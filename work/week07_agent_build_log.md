# Week 7 - Agent Build Log

## Starting point

The FL-06 spec chose a Claude Project with a read-only GitHub connector for a Weekly Evidence
Review Assistant. The core job was intentionally narrow: inspect one selected notebook, note what
the evidence supports, flag gaps and risks, and return three human actions. The agent must never
edit, commit, submit, publish, or deploy.

## Iteration log

### Attempt 1 - Claude Project + GitHub connector

I planned to connect the public repository in Claude Project settings and test a filename search for
`w05_model.ipynb`, followed by a read of the relevant modeling skill. That remains the intended
platform from the spec, but this VS Code session cannot authenticate or configure my external Claude
account. I could not honestly record a successful Claude connector run or a raw screen capture from
that account.

### Attempt 2 - Local read-only fallback

To get the core job working end to end in the available environment, I added
`scripts/weekly_review_agent.py`. It uses the repository filesystem as its live data connection.
It accepts one artifact and optional supporting files, reads Markdown or notebook JSON, checks for
saved outputs and claim-boundary language, reports simple risk signals, and prints the five-section
review memo. It has no write path and uses only Python’s standard library.

### What broke

- The external Claude/GitHub connector could not be authenticated from this workspace.
- The GitHub-backed workspace has no local terminal checkout, so I could not run the script through
  PowerShell from a filesystem path.
- The existing `w05_model.ipynb` was later changed and currently reports no executed cells in the
  notebook summary, so the agent must say “not verified” rather than repeat earlier metrics.

### What changed

- Added a deterministic local file reader for Markdown and `.ipynb` JSON.
- Added explicit output-verification status for notebooks.
- Added risk checks for sensitive terms and unsupported strong language.
- Added a fixed five-section memo and exactly three next actions.

### What I cut and why

- Cut dynamic GitHub search and commit-diff retrieval because the connector was unavailable here.
- Cut notebook execution because a review agent should not silently execute or mutate a user’s
  analysis in this MVP, and no local interpreter path is available to the terminal.
- Cut all write actions, scheduling, email, deployment, and repository changes because they were
  outside the core review job and conflict with the FL-06 guardrails.

## MVP acceptance check

The fallback agent is considered ready for a local run when this command is executed from a cloned
repository:

```powershell
python scripts/weekly_review_agent.py work/notebooks/w05_model.ipynb skills/training-honest-models/SKILL.md
```

Expected behavior is a memo with five headings. If the notebook has no saved outputs, the memo must
say **not verified** and recommend running the notebook; it must not call the model successful.

## Evidence still required from me

The assignment asks for a raw, unedited approximately two-minute capture of a successful run. I
cannot create an authentic external-account screen recording from this VS Code session. I must run
the command above in a local clone or configure the Claude Project connector, record the full request
through memo output without edits, and attach that original capture to the submission.