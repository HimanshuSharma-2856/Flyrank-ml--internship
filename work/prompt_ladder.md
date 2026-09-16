# Prompt Ladder: Framing the FlyRank Case

**Track:** Applied search intelligence and content-archetype analysis  
**Task:** Turn the FlyRank internship work into a useful case-study draft for a stranger.  
**Audience:** A content operations lead at an SEO or content agency managing a large page portfolio.  
**One action:** Email me to discuss a similar content-inventory problem.

## How I ran the ladder

I kept the task constant: produce a short explanation of the FlyRank project. I changed one prompt layer at a time and compared each output with the previous output. The excerpts below are representative captures of each run, kept short enough to compare side by side; they preserve the important behavior of the full response.

The starting evidence was the repository's Week 1 research-question notebook: 30,000 rows, 32 pseudonymized clients, three content types, and median word counts of 3,155 for comparison articles and 1,237 for Feedly articles. The project is descriptive decision support, not proof that a cluster causes better search performance.

## Run 0: Weak baseline

### Prompt

> Help me with my FlyRank project.

### Representative output

> The FlyRank project uses machine learning and data analysis to improve content performance. You could describe the project by explaining the problem, the methods you used, and the results. A strong portfolio piece should highlight your technical skills, business impact, and ability to turn data into actionable insights.

### Notes

- **What changed in the prompt:** Nothing was added; this is the deliberately weak baseline.
- **What improved in the output:** Nothing useful. It produced a generic project description that could fit almost any analytics portfolio.
- **What still failed:** It named no decision, audience, evidence, lane, dataset, or honest limitation. It also invented the idea of “business impact” without evidence.
- **What I would try next:** State the concrete goal of the writing task.

## Run 1: Clearer goal

### Single layer added

**Goal:** explain the project as a portfolio case study.

### Prompt

> Help me explain my FlyRank project as a short portfolio case study.

### Representative output

> **Problem:** Content teams need better ways to understand which pages need attention.  
> **Approach:** I analyzed content data with machine-learning methods to identify patterns and opportunities.  
> **Outcome:** The analysis created actionable insights that could support content improvements and more efficient review.

### Notes

- **What changed in the prompt:** I replaced the vague request with the goal of producing a portfolio case study.
- **What improved in the output:** It returned a usable three-part shape instead of general advice about writing a portfolio.
- **What still failed:** The output was still interchangeable with a marketing analytics project. The goal alone did not make it specific, and the phrase “created actionable insights” was unsupported.
- **What I would try next:** Name the person who needs this case study and what they need to decide.

## Run 2: Defined audience

### Single layer added

**Audience:** a content operations lead at an SEO or content agency managing a large page portfolio.

### Prompt

> Help me explain my FlyRank project as a short portfolio case study for a content operations lead at an SEO or content agency managing a large page portfolio.

### Representative output

> **Problem:** A content operations lead needs a consistent way to compare a large number of pages and decide where editorial review should start.  
> **Approach:** I analyzed page-level signals to find groups of pages with similar characteristics.  
> **Outcome:** The groups can help a content team prioritize review and apply a more relevant checklist to each group.

### Notes

- **What changed in the prompt:** I added one defined reader with a recurring operational decision.
- **What improved in the output:** It stopped explaining generic “content performance” and focused on comparing pages and choosing a review starting point.
- **What still failed:** **This did not help as much as expected.** The reader became clearer, but the method and evidence were still vague. “Page-level signals” and “the groups” could describe work I had not actually completed.
- **What I would try next:** Add the real project context so the reader can tell this is my FlyRank work.

## Run 3: Real context

### Single layer added

**Context:** the selected lane, dataset scale, measured structural contrast, and current evidence boundary.

### Prompt

> Help me explain my FlyRank project as a short portfolio case study for a content operations lead at an SEO or content agency managing a large page portfolio. Context: I chose Structured Content Archetype Clustering. The starter slice has 30,000 content-item rows across 32 pseudonymized clients and three content types. The median word count is 3,155 for comparison articles and 1,237 for Feedly articles. I am investigating whether observable structure can organize review; the current evidence is descriptive and does not prove that a cluster causes better search performance.

### Representative output

> FlyRank gave me a concrete question: can observable page structure help an editor compare like with like in a 30,000-row inventory? In the starter slice, comparison articles had a median word count of 3,155, while Feedly articles had a median of 1,237. I used that contrast to justify looking for interpretable page profiles, while keeping the claim narrow: this can organize review, but it does not show that one content type or cluster performs better.

### Notes

- **What changed in the prompt:** I added the actual lane, scale, structural finding, and claim boundary.
- **What improved in the output:** The project became recognizable as mine. It used the real numbers and connected them to the editorial decision instead of asserting generic impact.
- **What still failed:** It was a strong paragraph, but not yet a complete case study. It did not clearly separate the problem, decisions made, and outcome or tell the reader what to do next.
- **What I would try next:** Specify the output format.

## Run 4: Specified output format

### Single layer added

**Format:** three headings, `The problem`, `What I did`, and `What came of it`, followed by one CTA.

### Prompt

> Help me explain my FlyRank project as a short portfolio case study for a content operations lead at an SEO or content agency managing a large page portfolio. Context: I chose Structured Content Archetype Clustering. The starter slice has 30,000 content-item rows across 32 pseudonymized clients and three content types. The median word count is 3,155 for comparison articles and 1,237 for Feedly articles. I am investigating whether observable structure can organize review; the current evidence is descriptive and does not prove that a cluster causes better search performance. Format the response with exactly these headings: `The problem`, `What I did`, and `What came of it`. End with one sentence inviting the reader to email me about a similar content-inventory problem.

### Representative output

> ### The problem  
> Reviewing a large page portfolio one URL at a time makes it hard to compare similar work or choose the right checklist first. I asked whether observable structure could help an editor organize that review.
>
> ### What I did  
> I chose Structured Content Archetype Clustering and examined content type, search intent, word count, content age, and update recency. The 30,000-row starter slice spans 32 pseudonymized clients and three content types. Comparison articles had a median word count of 3,155 versus 1,237 for Feedly articles. I treated that as a reason to compare like with like, not as evidence that one format performs better.
>
> ### What came of it  
> The work produced a defensible way to investigate page profiles and choose a review approach. It remains decision support: a reviewer should sample a group before changing pages, and the analysis does not prove causal effects on rankings, traffic, clicks, or conversions.
>
> Email me to discuss a similar content-inventory problem.

### Notes

- **What changed in the prompt:** I required a fixed three-beat structure and one final action.
- **What improved in the output:** The reader can scan the case and understand the question, decisions, evidence, limit, and next step without reconstructing the story.
- **What still failed:** The structure made the writing cleaner, but it did not by itself prevent inflated language such as “produced a defensible way” or ensure that every claim was tied to a notebook check.
- **What I would try next:** Add explicit constraints about evidence, privacy, causal language, and what not to invent.

## Run 5: Constraints

### Single layer added

**Constraints:** use only supplied evidence; avoid causal claims; do not invent completed clusters, client names, metrics, or outcomes; keep the recommendation human-reviewed and public-safe.

### Prompt

> Help me explain my FlyRank project as a short portfolio case study for a content operations lead at an SEO or content agency managing a large page portfolio. Context: I chose Structured Content Archetype Clustering. The starter slice has 30,000 content-item rows across 32 pseudonymized clients and three content types. The median word count is 3,155 for comparison articles and 1,237 for Feedly articles. I am investigating whether observable structure can organize review; the current evidence is descriptive and does not prove that a cluster causes better search performance. Format the response with exactly these headings: `The problem`, `What I did`, and `What came of it`. End with one sentence inviting the reader to email me about a similar content-inventory problem. Constraints: use only the facts supplied here and the linked Week 1 notebook; do not invent completed clusters, client names, model performance, business impact, or personal experience; do not imply that content type or cluster causes better SEO outcomes; keep the recommendation as a human review step; use plain, specific language and no buzzwords.

### Representative output

> ### The problem  
> A large page portfolio is hard to review consistently. An editor can inspect pages one at a time, but that makes it difficult to compare similar work and decide which review approach belongs first. I asked whether observable structure could organize that decision.
>
> ### What I did  
> I chose Structured Content Archetype Clustering and investigated observable structure such as content type, search intent, word count, content age, and update recency. The starter slice contains 30,000 content-item rows across 32 pseudonymized clients and three content types. Comparison articles have a median word count of 3,155, compared with 1,237 for Feedly articles. That is a measured difference worth checking, not proof that either format performs better. The work is still an investigation into interpretable profiles; it is not a claim that completed clusters already determine what to rewrite.
>
> ### What came of it  
> So far, the project has narrowed a vague clustering idea into a review question with a human checkpoint: compare like with like, sample any proposed group, and decide what to inspect next. The available evidence supports descriptive decision support only. It does not establish that a cluster causes better rankings, traffic, clicks, or conversions.
>
> Email me to discuss a similar content-inventory problem.

### Notes

- **What changed in the prompt:** I added evidence, privacy, anti-invention, anti-causal, human-review, and plain-language constraints.
- **What improved in the output:** It stopped implying that completed clusters or business impact already existed. The outcome now matches the actual notebook evidence and keeps the next action usable.
- **What still failed:** Constraints did not make the result more vivid; they made it more cautious. The case still needs later notebook results if I want to claim validated clusters rather than a well-framed investigation.
- **What I would try next:** Keep these constraints and add verified later results only after they exist.

## Final reusable prompt

Use this prompt when a stranger needs to turn a similar FlyRank analysis into a case study:

> Write a short portfolio case study for a content operations lead at an SEO or content agency managing a large page portfolio. Use exactly three headings: `The problem`, `What I did`, and `What came of it`, followed by one sentence inviting the reader to email me about a similar content-inventory problem.
>
> Project context: I chose Structured Content Archetype Clustering. The starter slice contains 30,000 content-item rows across 32 pseudonymized clients and three content types. The median word count is 3,155 for comparison articles and 1,237 for Feedly articles. I am investigating whether observable page structure can organize review. The current evidence is descriptive and does not prove that a cluster causes better search performance.
>
> Use only the facts supplied here and the linked notebook. Do not invent completed clusters, client names, metrics, business impact, outcomes, or personal experience. Do not imply that content type or cluster causes better rankings, traffic, clicks, or conversions. Keep the recommendation as a human review step. Use direct, warm, plain, specific, evidence-led language with no buzzwords. If the evidence only supports an investigation, say “so far” and do not write as though the final result already exists.

## Ladder verdict

The audience layer improved relevance but did not make the case specific. The context layer earned the largest improvement because it supplied the actual evidence. The format layer made the result scannable. The constraints layer made the case more honest, even though it also made the prose less flashy. The final prompt works without this document because it names the reader, evidence, structure, boundaries, and action explicitly.