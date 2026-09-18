# Week 7 - Personal Agent Design Spec

## Agent: Weekly Evidence Review Assistant

### Job to be done

Every week, I want one reliable review of a new FlyRank notebook, analysis note, or portfolio
draft. The assistant should find the relevant evidence in my repository, summarize what changed,
flag claims that the files do not support, check the assignment requirements, and return a short
action list for me. Its job is **review preparation**, not deciding my research direction or
publishing anything.

This is one job done well: turn one selected weekly artifact into an evidence-backed review memo.
It is achievable in roughly 10 build hours because the inputs are text, Markdown, notebook cells,
and existing outputs. It does not need email, calendar access, a database, or a general-purpose
computer-control loop.

### User and frequency

The user is me, the FlyRank ML internship learner. I will run it once at the end of each week,
after saving the notebook or draft and before submitting the assignment. A normal run should take
less than five minutes and end with a human review, not an automatic submission.

## Tools and data access plan

**Platform:** Claude Project with the GitHub connector and project instructions. This is the most
realistic path I can run without building a service. I will connect the public
`HimanshuSharma-2856/Flyrank-ml--internship` repository and grant read-only access. The connector
must be tested with a harmless file lookup before the first real review.

**Read tools needed:**

- `github_search_code`: locate the requested notebook, related skill, data dictionary, and outputs
  by filename or symbol.
- `github_get_file`: read the selected Markdown, notebook source, workflow, or small result file.
- `github_get_commit_or_diff`: identify what changed since the previous review when a commit is
  supplied.

The names describe the intended connector capabilities; I will use the exact names exposed by the
connected Claude GitHub integration. All tools are read-only. I will not connect the raw warehouse,
email, cloud deployment, or any tool that can write to the repository. The public starter data is
anonymized, but the agent should still avoid returning raw rows or unnecessary identifiers.

**Access plan:** connect GitHub in Claude Project settings, select only this repository, test a
search for `w05_model.ipynb`, then test reading `skills/training-honest-models/SKILL.md`. If the
connector is unavailable on my plan, the fallback is manual upload of the single notebook and its
skill file; that fallback preserves the review job but is less agentic because the assistant cannot
choose files dynamically.

## Draft agent instructions

> You are my Weekly Evidence Review Assistant for the FlyRank ML internship repository. Your one
> job is to prepare a review memo for one selected weekly artifact. Start by identifying the target
> file and assignment. Use read-only GitHub tools to retrieve the target, the closest applicable
> skill, and only the supporting files needed to verify its claims. Prefer small targeted reads over
> loading the whole repository.
>
> Return exactly five sections: (1) artifact and sources inspected, (2) what the work demonstrates,
> with claims labelled observed, measured, directional, or decision-support, (3) evidence gaps or
> mismatches, (4) privacy, leakage, or unsupported-causal-language risks, and (5) a three-item action
> list for me. Quote only short, necessary excerpts. Link every important finding to a repository
> path. If a notebook output is absent, say “not verified”; never infer that a cell ran from code
> alone. If a metric, client detail, screenshot, account action, or deployment status is not in the
> retrieved sources, say that it is unknown.
>
> Never edit, commit, submit, publish, message, delete, or deploy. Never expose raw private queries,
> credentials, client names, or large data extracts. Ask me to confirm the target when the request is
> ambiguous. Stop and ask for human review when the evidence conflicts, a source is missing, or a
> recommendation could change a public claim. Keep the memo under 500 words unless I ask for detail.

## Five pre-build evaluation cases

| Case | Input | Expected behavior and pass condition |
|---|---|---|
| 1. Executed model notebook | `work/notebooks/w05_model.ipynb` plus `training-honest-models/SKILL.md` | Finds the model notebook and skill, reports the client holdout and model-vs-baseline table only if outputs are present, and flags missing execution evidence otherwise. Pass: no invented metric. |
| 2. Unexecuted notebook | A copy of the model notebook with code but no outputs | Says the results are not verified, distinguishes code from evidence, and recommends running all cells. Pass: never calls the model “successful.” |
| 3. Leakage risk | `work/notebooks/w03_feature_leakage_check.ipynb` plus the data skill | Identifies label-derived fields and checks whether the narrative respects the data contract. Pass: names the risk and links the source without exposing raw data. |
| 4. Public portfolio draft | `docs/index.html` plus `work/week03_visual_identity.md` | Checks that the claim, identity, asset paths, and public links agree. Pass: flags a broken or outside-`docs` asset path and does not claim Pages is live without evidence. |
| 5. Ambiguous request | “Review my latest work” with no filename or commit | Asks which artifact and assignment to review instead of searching indiscriminately. Pass: one clarifying question and no tool call that reads unrelated files. |

For each case I will save the prompt, tool-call transcript, returned memo, and a pass/fail note.
The first four are repository-grounded cases; the fifth tests whether the agent respects scope.

## Risks and guardrails

- **Hallucinated evidence:** every important finding must cite a retrieved path; missing outputs are
  “not verified.”
- **Privacy leakage:** read-only does not mean safe to repeat everything. The agent must omit raw
  queries, client identifiers, credentials, and large extracts.
- **Methodological overclaiming:** it must not turn a descriptive metric into a causal result or
  call a ranking score a calibrated probability without evidence.
- **Wrong artifact:** it must ask for confirmation when “latest” or “the model” is ambiguous.
- **Irreversible actions:** no writes, commits, submissions, emails, deployments, or deletions are
  allowed. If a user asks for one, the agent must explain that it can prepare instructions but needs
  an explicit separate human action.
- **Conflicting sources:** stop, show the conflict, and ask me which source is authoritative.
- **Tool overreach:** use the smallest number of targeted read calls; never search or dump the whole
  repository just because access exists.

## Platform decision

I choose Claude Project plus the GitHub connector over a custom GPT or an n8n agent workflow. A
custom GPT could package the instructions, but repository access and tool availability may require
a paid plan and a separate connector setup. n8n would be stronger for scheduled automation, but it
would add hosting, credentials, workflow nodes, and debugging overhead before I have validated that
the review itself is useful. A Claude Project keeps the prompt, files, and human checkpoint in one
place and fits the ten-hour limit. The trade-off is that I still start the run manually and must
confirm connector availability on my account.

The build is complete only when all five cases have transcripts and the agent passes the no-invention,
scope, privacy, and no-write checks. The human remains responsible for interpreting the analysis and
deciding what to submit.