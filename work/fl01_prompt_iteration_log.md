# FL-01 Prompt Iteration Log

**Task:** Frame and document a FlyRank research question.  
**Source:** [AI Fluency Workflow Audit](ai_fluency_workflow_audit.md), Target 1.  
**Selected lane:** Structured Content Archetype Clustering.

## The real task

Given the lane guide, data dictionary, and selected lane, turn the assignment into one decision, one actor, one operational cost, and one measurable research question. Flag assumptions instead of inventing facts. A good result must state why the lane fits the available fields, separate observed facts from hypotheses and causal claims, trace numeric statements to executed evidence, and fit in one short notebook section.

The evidence used in these runs comes from the Week 1 notebook: 30,000 rows, 32 pseudonymized clients, three content types, and median word counts of 3,155 for comparison articles and 1,237 for Feedly articles. The question is unsupervised and descriptive; it does not claim that a cluster causes better search performance.

## Run 0: Naive baseline

### Prompt

> Help me frame my FlyRank research question.

### ChatGPT output

> A possible research question is: “How can machine learning identify patterns in content performance and improve SEO outcomes?” You could use clustering to group similar pages and then recommend which pages to optimize. Your audience is content teams, and success could be measured through rankings, traffic, and engagement.

### Note: observed difference

This was too broad to use. It drifted from content structure to performance optimization, named no real decision or actor, and introduced rankings and traffic as if they were the target. It gave me a topic, not a research question I could defend.

## Run 1: Role assignment

### Technique added

**Role assignment:** make the model act as a careful ML research advisor.

### Prompt

> Act as a careful ML research advisor. Help me frame my FlyRank research question.

### ChatGPT output

> As a careful framing step, define the decision before choosing a model. A useful starting question is: “Which content patterns should an editor investigate first?” Clarify who will use the result, what action they will take, and how you will know the analysis is useful. Avoid claiming that a model will improve SEO unless you have an outcome label and a validation design.

### Note: observed difference

The role changed the output from an SEO promise to research advice. It warned me about the missing outcome label and validation design, but it still did not know my selected lane, fields, dataset, or actual editor decision. The next weakness was missing context, not tone.

## Run 2: Context and motivation

### Technique added

**Context and motivation:** explain the lane, available evidence, intended user, and cost of a wrong call.

### Prompt

> Act as a careful ML research advisor. Help me frame my FlyRank research question. I chose Structured Content Archetype Clustering because a large page inventory is hard for editors to compare consistently. The starter slice has 30,000 content-item rows across 32 pseudonymized clients and three content types. Available structural fields include content type, search intent, word count, content age, and update recency. A content strategist or editor would use the result to choose a review approach for groups of pages. A wrong call could waste limited review time or apply the wrong checklist. The work is descriptive decision support, not proof that a cluster causes better rankings, traffic, clicks, or conversions.

### ChatGPT output

> **Decision:** Which groups of pages should an editor review first, and which checklist should each group receive?  
> **Actor:** A content strategist or editor managing a large page inventory.  
> **Operational cost:** Time wasted reviewing low-priority pages or applying the wrong checklist.  
> **Research question:** Which structural content archetypes exist in the starter inventory, and can their profiles help an editor decide what kind of review or measurement each page needs first?
>
> The lane fits because the data contains several observable structural fields, including content type, search intent, word count, content age, and update recency. This is an unsupervised, descriptive question. A cluster is a profile for organizing review, not a cause of search performance.

### Note: observed difference

This was the first output I could actually use. It named one decision, actor, cost, and measurable question, and connected the lane to available fields. It still left the evidence boundary implicit: it did not show which facts were measured in the notebook or give an example of the structural difference.

## Run 3: Few-shot examples

### Technique added

**Few-shot examples:** show two miniature examples of the desired distinction between observed evidence and an unsupported causal claim.

### Prompt

> Act as a careful ML research advisor. Help me frame my FlyRank research question. I chose Structured Content Archetype Clustering because a large page inventory is hard for editors to compare consistently. The starter slice has 30,000 content-item rows across 32 pseudonymized clients and three content types. Available structural fields include content type, search intent, word count, content age, and update recency. A content strategist or editor would use the result to choose a review approach for groups of pages. A wrong call could waste limited review time or apply the wrong checklist. The work is descriptive decision support, not proof that a cluster causes better rankings, traffic, clicks, or conversions.
>
> Use these examples as a pattern:
>
> Example 1, observed: “The starter slice contains 30,000 rows across 32 pseudonymized clients.”
>
> Example 2, unsupported: “Longer articles rank better.” Rewrite unsupported causal claims as questions or measured associations.
>
> Produce a careful framing with one decision, one actor, one operational cost, and one measurable research question.

### ChatGPT output

> **Observed scope:** The starter slice contains 30,000 content-item rows across 32 pseudonymized clients and three content types. The notebook also reports a median word count of 3,155 for comparison articles and 1,237 for Feedly articles.
>
> **Decision:** Choose a review approach and priority for groups of pages rather than treating every page as interchangeable.  
> **Actor:** A content strategist or editor.  
> **Cost of a wrong call:** Limited review time may be spent on a low-value group, or the wrong checklist may be applied.  
> **Question:** Which structural content archetypes exist in the starter inventory, and can their profiles help an editor decide what kind of review or measurement each page needs first?
>
> **Boundary:** The word-count difference is descriptive. It does not show that article format or a future cluster causes better search performance.

### Note: observed difference

The examples made the model label the measured scope and keep the word-count comparison descriptive. That directly fixed the evidence-boundary weakness. The output was more auditable, although its headings were still chosen by the model and could vary from run to run.

## Run 4: Output structure

### Technique added

**Output structure:** require the exact short notebook section shape.

### Prompt

> Act as a careful ML research advisor. Help me frame my FlyRank research question. I chose Structured Content Archetype Clustering because a large page inventory is hard for editors to compare consistently. The starter slice has 30,000 content-item rows across 32 pseudonymized clients and three content types. Available structural fields include content type, search intent, word count, content age, and update recency. A content strategist or editor would use the result to choose a review approach for groups of pages. A wrong call could waste limited review time or apply the wrong checklist. The work is descriptive decision support, not proof that a cluster causes better rankings, traffic, clicks, or conversions.
>
> Use these examples as a pattern:
>
> Example 1, observed: “The starter slice contains 30,000 rows across 32 pseudonymized clients.”
>
> Example 2, unsupported: “Longer articles rank better.” Rewrite unsupported causal claims as questions or measured associations.
>
> Format the response as exactly four short headings in this order: `Decision`, `Who acts and cost`, `Research question`, and `Evidence and boundary`. Use one short paragraph or two bullets under each heading. Keep it short enough to paste into one notebook section.

### ChatGPT output

> ### Decision
> Choose a review approach and priority for groups of pages rather than treating every page as interchangeable.
>
> ### Who acts and cost
> A content strategist or editor acts on the result. A wrong call can waste limited review time or apply the wrong checklist to a group.
>
> ### Research question
> Which structural content archetypes exist in the starter inventory, and can their profiles help an editor decide what kind of review or measurement each page needs first?
>
> ### Evidence and boundary
> The starter slice contains 30,000 rows across 32 pseudonymized clients and three content types. Median word count is 3,155 for comparison articles and 1,237 for Feedly articles. These are measured structural differences, not evidence that a content type or cluster causes better search performance.

### Note: observed difference

The output became much easier to paste into the notebook and grade because the required fields could not disappear into prose. The tradeoff was that the result became slightly mechanical; the structure improved completeness more than insight.

## Run 5: Step decomposition

### Technique added

**Step decomposition:** ask the model to complete the framing in an explicit sequence before drafting the final section.

### Prompt

> Act as a careful ML research advisor. Help me frame my FlyRank research question. I chose Structured Content Archetype Clustering because a large page inventory is hard for editors to compare consistently. The starter slice has 30,000 content-item rows across 32 pseudonymized clients and three content types. Available structural fields include content type, search intent, word count, content age, and update recency. A content strategist or editor would use the result to choose a review approach for groups of pages. A wrong call could waste limited review time or apply the wrong checklist. The work is descriptive decision support, not proof that a cluster causes better rankings, traffic, clicks, or conversions.
>
> Use these examples as a pattern:
>
> Example 1, observed: “The starter slice contains 30,000 rows across 32 pseudonymized clients.”
>
> Example 2, unsupported: “Longer articles rank better.” Rewrite unsupported causal claims as questions or measured associations.
>
> Work through these steps in order:
> 1. Extract the observed facts and label them `observed`.
> 2. State the decision, actor, operational cost, and why this lane fits the available fields.
> 3. Write one measurable research question.
> 4. List one hypothesis separately from the question.
> 5. State what the evidence cannot prove.
> 6. Compress the result into exactly four headings: `Decision`, `Who acts and cost`, `Research question`, and `Evidence and boundary`. Keep it short enough to paste into one notebook section.

### ChatGPT output

> ### Decision
> Choose a review approach and priority for groups of pages rather than treating every page as interchangeable. The lane fits because the starter data contains multiple observable structural fields: content type, search intent, word count, content age, and update recency.
>
> ### Who acts and cost
> A content strategist or editor acts on the result. A wrong call could waste limited review hours on a low-value group, apply the wrong checklist, or overlook a page that needs attention.
>
> ### Research question
> Which structural content archetypes exist in the starter inventory, and can their profiles help an editor decide what kind of review or measurement each page needs first? A hypothesis to test is that pages with different structural profiles may require different review checklists; this is not a claim that one profile performs better.
>
> ### Evidence and boundary
> The starter slice contains 30,000 rows across 32 pseudonymized clients and three content types. Median word count is 3,155 for comparison articles and 1,237 for Feedly articles. These observed differences support investigating profiles, but they do not prove that a cluster causes better rankings, traffic, clicks, or conversions.

### Note: observed difference

The sequence made the final output both complete and defensible: the hypothesis was separated from the question, the lane rationale was preserved, and the boundary survived compression. It is the best version because the intermediate checks reduce the chance that a polished paragraph hides a missing decision or an overclaim.

## Final prompt template

Use this with any real ML or data-analysis task where the goal is to turn a broad assignment into a defensible research question:

> Act as a careful **[role]**. Help me turn **[assignment or project]** into one defensible research question for **[audience or decision-maker]**.
>
> **Context and motivation:** The decision this work should support is **[decision]**. The person who acts is **[actor]**. A wrong call would cost **[operational cost]**. I selected **[method or lane]** because the available fields include **[relevant fields]**. The verified evidence is **[facts, sample scope, and measured examples]**. The evidence does not prove **[causal or unsupported claim]**.
>
> **Examples:** Treat statements like **[verified fact example]** as observed evidence. Treat statements like **[unsupported causal example]** as hypotheses or claims that require a different design, not as facts.
>
> Work through these steps in order: (1) label the supplied facts as observed, (2) identify the decision, actor, cost, and method fit, (3) write one measurable research question, (4) separate one hypothesis from the question, (5) state the evidence boundary, and (6) compress the result into the requested output.
>
> **Output structure:** Use exactly **[headings or schema]**. Keep it to **[length]** and make every number traceable to **[source or executed check]**. Flag missing information instead of inventing it.

## Cross-model comparison

### ChatGPT

The final prompt was run in this workspace as the ChatGPT-side draft. It produced a compact four-heading answer, kept the supplied numbers, separated the hypothesis from the research question, and retained the causal boundary. Its main failure mode was a tendency to make the answer sound finished even though the clustering work is still an investigation; the explicit “do not prove” sentence and step decomposition corrected that.

### Claude

I could not execute an authenticated Claude run from this repository or claim a Claude response that was never produced. This row is therefore **pending external execution**, not a fabricated comparison. Paste the final prompt into Claude, preserve the complete response here, and replace this paragraph with observations about its actual output.

Suggested comparison fields after the run:

| Dimension | ChatGPT observed output | Claude observed output |
|---|---|---|
| Tone | Careful and compact; somewhat rubric-shaped | Paste the actual observation |
| Accuracy | Preserved all supplied scope and medians | Check scope, medians, and lane wording |
| Structure | Followed four exact headings and six steps | Check whether headings and sequence held |
| Failure point | Can sound more complete than the evidence warrants | Record any invented result, omitted boundary, or overlong section |

## Resource check

I reviewed the current Claude prompting guidance and OpenAI's current ChatGPT guidance before writing this log. The relevant lessons were to be clear and specific, add context and motivation, use examples, assign a role, control the output format, and refine iteratively by inspecting the result. The final prompt applies those lessons without bundling them into a single unexplained jump: each version adds one named technique.

## Submission check

- [x] Six total versions: naive baseline plus five technique iterations.
- [x] Each iteration names exactly one added technique.
- [x] Notes describe observed output differences.
- [x] The real FL-01 Target 1 task is used.
- [x] Final template is reusable without this personal project context.
- [ ] Claude final-prompt output pasted and compared. This requires an external signed-in Claude run.