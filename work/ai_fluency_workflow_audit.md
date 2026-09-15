# AI Fluency Workflow Audit

**Scope:** FlyRank internship work completed and in progress during this week  
**Selected lane:** Structured Content Archetype Clustering  
**Audit principle:** AI can draft, organize, explain, and check work; I retain responsibility for problem choice, sensitive judgment, evidence, and final submission.

## 1. Recurring-task audit

The tasks below are grounded in the FlyRank work visible in this repository and in the current assignment. They are intentionally specific rather than generic examples.

| Recurring task | Classification | Why |
|---|---|---|
| Choose the ML lane that best fits my interests and the available data | Just me | The choice determines the research direction and must reflect my judgment about what I can sustain and explain. |
| Turn a broad assignment brief into a concrete research question | Collaborate with AI | AI can expose missing decision, actor, and cost details, but I must decide whether the question is meaningful. |
| Read the dataset guide and data dictionary before analysis | Collaborate with AI | AI can summarize definitions and caveats, while I must notice ambiguity that could change the analysis. |
| Load the starter CSV and inspect row, client, and content-type counts | Delegate to AI with review | Code generation is repeatable, but I review paths, column names, counts, and unexpected missingness. |
| Select and explain observable features for content archetype clustering | Collaborate with AI | AI can suggest candidate features and tradeoffs; I decide whether each feature represents the research question. |
| Write the notebook narrative connecting evidence to the decision | Collaborate with AI | AI can draft readable prose, but I must verify that every sentence matches an observed result. |
| Add executable assertions and validation messages to the notebook | Delegate to AI with review | AI can write mechanical checks quickly; I choose the invariants and inspect the resulting output. |
| Run the notebook from top to bottom | Delegate to AI with review | Execution can be automated, but I must read outputs and investigate errors instead of treating a green run as proof. |
| Debug the notebook kernel and data-loading path | Delegate to AI with review | AI can diagnose environment errors and propose a fallback; I confirm that the fallback uses the intended public file. |
| Decide which claims are descriptive, directional, or unsupported | Just me | This is the boundary of what I am willing to claim publicly and cannot be delegated to a fluent draft. |
| Check the work for client-identifying details, private queries, and causal overclaiming | Just me | I am accountable for privacy and research integrity, even when an AI assistant performs the initial scan. |
| Convert the assignment requirements into a submission checklist and final artifact | Delegate to AI with review | AI is useful for coverage checks; I confirm that the deliverable is genuinely mine and that evidence is attached. |

### Decision rule

I will use AI more freely for reversible, inspectable work such as drafting code, restructuring prose, and generating checklists. I will keep human control over research direction, privacy, ethical boundaries, interpretation, and final submission. I will not fully automate any task in this audit because the current work contains judgment-heavy claims and public-facing analysis.

## 2. Three reusable target tasks for FL-02 through FL-04

### Target 1: Frame and document a FlyRank research question

**Reusable prompt/task:** Given the current lane guide, data dictionary, and my selected lane, help me turn the assignment into a decision, actor, cost, and measurable research question. Flag assumptions instead of inventing facts.

**Done well means:**

- The output names one decision, one actor, one operational cost, and one measurable question.
- It states the selected lane and why it fits the available fields.
- It separates observed facts from hypotheses and causal claims.
- I can trace every numeric statement to an executed notebook cell or cited repository file.
- The final framing fits in one short notebook section and survives my review without unsupported claims.

### Target 2: Produce and validate a small data-backed notebook section

**Reusable prompt/task:** Help me write or repair a notebook section that loads the starter data, computes the requested summary, and includes assertions that catch an invalid or incomplete result.

**Done well means:**

- Every code cell runs top to bottom in a clean kernel with no errors.
- The section includes at least three relevant measured outputs and at least two executable assertions.
- The output reports the actual sample scope, including row and group counts where relevant.
- The assistant does not silently change the data source, target, or feature definition.
- I inspect the output and can explain what each assertion protects against.

### Target 3: Turn verified work into a public-safe submission artifact

**Reusable prompt/task:** Compare my draft against the assignment rubric, identify missing evidence or overclaims, and produce a concise table-format submission without adding private or fabricated details.

**Done well means:**

- The artifact covers every rubric requirement with a visible checklist or table row.
- It contains no client names, private queries, credentials, or unsupported causal language.
- Each important claim is labeled as observed, measured, directional, or decision-support.
- It is no longer than two pages when rendered in normal Markdown/PDF formatting.
- A final human review confirms that the wording, screenshots, and account evidence are authentic.

## 3. Toolkit and evidence checklist

The repository can document my AI-assisted work, but it cannot verify external account ownership, course enrollment, or screenshots. I must complete and attach those items myself.

| Requirement | Status | Evidence to attach |
|---|---|---|
| Claude account | Pending user setup | Screenshot showing the signed-in Claude account, with personal identifiers minimized where possible. |
| ChatGPT account | Pending user setup | Screenshot showing the signed-in ChatGPT account, with personal identifiers minimized where possible. |
| Anthropic Academy account | Pending user setup | Screenshot showing the signed-in Academy account or course dashboard. |
| Enroll in *AI Fluency: Framework & Foundations* | Pending user setup | Course enrollment or dashboard screenshot. |
| Complete at least the first module | Pending user completion | Completion marker, certificate progress, or module-status screenshot. |
| Create one Claude Project | Pending user setup | Screenshot of the Project overview. |
| Configure Project instructions | Draft provided below; screenshot pending | Screenshot of the saved instructions and Project name. |

### Claude Project instructions to paste

> I am a FlyRank ML internship learner working on a structured content archetype clustering project. I value careful, plain-language reasoning and evidence that can be reproduced from the repository. Use a concise, constructive tone. Help me frame questions, draft inspectable Python and Markdown, find missing assumptions, and build checklists. Ask before making large changes. Never invent personal experience, metrics, account setup, screenshots, client details, or source evidence. Treat my research direction, privacy decisions, ethical boundaries, interpretation, and final submission as mine to decide. Prefer the words observed, measured, directional, and decision-support when they are accurate. When reviewing a notebook, check that it runs top to bottom, that assertions protect meaningful invariants, and that claims match executed outputs.

## Submission note

This file is the completed workflow-audit draft. The external evidence rows remain intentionally pending until I perform the account, course, and Claude Project setup and add the screenshots. The repository evidence supporting the FlyRank tasks includes the completed Week 1 research-question notebook and its successful executable validation.