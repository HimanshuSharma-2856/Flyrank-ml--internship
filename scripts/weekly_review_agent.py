"""Read-only weekly evidence review agent.

This is the local fallback for the Claude Project + GitHub connector design. It uses the
filesystem as its live data source and emits a review memo; it never edits, commits, or
publishes repository content.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


FORBIDDEN_TERMS = ("password", "secret", "token", "api_key", "private query", "credential")
CLAIM_LABELS = ("observed", "measured", "directional", "decision-support", "hypothesis")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review one repository artifact without writing to it.")
    parser.add_argument("artifact", type=Path, help="Artifact to review.")
    parser.add_argument("supporting", nargs="*", type=Path, help="Optional supporting files.")
    return parser.parse_args()


def read_artifact(path: Path) -> tuple[str, dict[str, Any]]:
    """Read text or notebook source and return safe metadata plus searchable content."""
    if not path.exists():
        raise FileNotFoundError(f"Artifact not found: {path}")
    if path.suffix == ".ipynb":
        notebook = json.loads(path.read_text(encoding="utf-8"))
        cells = notebook.get("cells", [])
        source_parts: list[str] = []
        executed_code = 0
        output_cells = 0
        for cell in cells:
            source = "".join(cell.get("source", []))
            source_parts.append(source)
            if cell.get("cell_type") == "code":
                if source.strip():
                    executed_code += 1
                if cell.get("outputs"):
                    output_cells += 1
        content = "\n".join(source_parts)
        metadata = {
            "kind": "notebook",
            "cells": len(cells),
            "code_cells": executed_code,
            "output_cells": output_cells,
            "outputs_verified": output_cells > 0,
        }
        return content, metadata
    content = path.read_text(encoding="utf-8")
    return content, {"kind": "text", "characters": len(content), "outputs_verified": True}


def safe_findings(content: str, metadata: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    labels = [label for label in CLAIM_LABELS if label in content.lower()]
    if labels:
        findings.append(f"The artifact uses claim-boundary language: {', '.join(labels)}.")
    if metadata["kind"] == "notebook" and not metadata["outputs_verified"]:
        findings.append("Notebook outputs are not verified; code alone does not prove that the analysis ran.")
    elif metadata["kind"] == "notebook":
        findings.append(f"Notebook contains {metadata['output_cells']} cell(s) with saved output.")
    if "assert " in content:
        findings.append("The artifact contains executable assertions that can protect stated invariants.")
    return findings or ["No supported claim or verification signal was found in the selected source."]


def risk_findings(content: str, metadata: dict[str, Any]) -> list[str]:
    risks: list[str] = []
    lowered = content.lower()
    if any(term in lowered for term in FORBIDDEN_TERMS):
        risks.append("Review the source manually for sensitive terms before sharing the memo publicly.")
    if any(term in lowered for term in ("causes", "proves", "guarantees", "always")):
        risks.append("Check strong causal or universal language against the available evidence.")
    if metadata["kind"] == "notebook" and not metadata["outputs_verified"]:
        risks.append("Do not report metrics or successful execution until the notebook has been run and saved.")
    return risks or ["No automated risk signal found; human privacy and claim review is still required."]


def build_memo(artifact: Path, supporting: list[Path], content: str, metadata: dict[str, Any]) -> str:
    source_lines = [f"- `{artifact.as_posix()}` ({metadata['kind']})"]
    source_lines.extend(f"- `{path.as_posix()}` (supporting source)" for path in supporting)
    findings = safe_findings(content, metadata)
    risks = risk_findings(content, metadata)
    verification = "verified" if metadata["outputs_verified"] else "not verified"
    actions = [
        f"Confirm the selected artifact is the intended assignment and its outputs are {verification}.",
        "Trace each public claim to a source path and remove unsupported causal wording.",
        "Perform the final human privacy review before submitting or publishing anything.",
    ]
    return "\n".join(
        [
            "# Weekly Evidence Review Memo",
            "",
            "## 1. Artifact and sources inspected",
            *source_lines,
            "",
            "## 2. What the work demonstrates",
            *[f"- {finding}" for finding in findings],
            "",
            "## 3. Evidence gaps or mismatches",
            f"- Notebook execution status: **{verification}**.",
            "- This read-only runner checks source structure; it does not execute notebooks or validate external URLs.",
            "",
            "## 4. Privacy, leakage, or unsupported-causal-language risks",
            *[f"- {risk}" for risk in risks],
            "",
            "## 5. Three-item action list",
            *[f"{index}. {action}" for index, action in enumerate(actions, start=1)],
        ]
    )


def main() -> None:
    args = parse_args()
    content, metadata = read_artifact(args.artifact)
    missing_support = [path for path in args.supporting if not path.exists()]
    if missing_support:
        raise FileNotFoundError(f"Supporting source not found: {missing_support[0]}")
    print(build_memo(args.artifact, args.supporting, content, metadata))


if __name__ == "__main__":
    main()