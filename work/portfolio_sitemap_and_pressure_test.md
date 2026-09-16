# Portfolio Sitemap and Claude Project Setup

**Build:** FlyRank ML portfolio  
**Audience:** A content operations lead at an SEO or content agency managing a large page portfolio  
**One action:** Email me to discuss a similar content-inventory problem  
**Proof statement:** I can perform content-archetype analysis: I can use observable page structure to group a large content inventory into interpretable page profiles that help a content operations lead compare pages and decide what deserves review first. The work is descriptive decision support, not proof that a cluster causes better search performance.

**Voice card:** Direct, warm, plain, specific, evidence-led

**Visual identity standing instruction:** Use DM Sans for headings, body text, labels, and buttons, with IBM Plex Mono only for code, measured values, and compact metadata. Use `#17201D` near-black text, `#F8F7F2` warm white, `#145C52` deep green, and `#E3A84B` as the only accent; keep the mood calm, precise, and editorial so the analysis, numbers, and screenshots remain the most memorable part of the portfolio.

## 1. Small sitemap

Every page earns its place by moving one skeptical visitor from the claim to the one action.

```text
[LANDING]
Claim + selected finding + "Read the case study"
       |
       v
[WORK / CASE STUDY]
Question -> data -> method -> evidence -> limits -> "Discuss a similar problem"
       |                                      |
       v                                      v
   [ABOUT]                                [CONTACT]
   Who I am,                               One clear way to reach me
   what I value                            and propose a conversation
```

| Page | What the visitor must believe | What earns the page | Primary action |
|---|---|---|---|
| Landing | I have a specific, evidence-led way to improve content review. | The proof statement, one measured finding, and a visible path into the work. | Read the case study. |
| Work / Case Study | The claim is backed by a real question, reproducible analysis, and honest limits. | The FlyRank project: question, lane, data scope, structural features, validation, and decision use. | Discuss a similar problem. |
| About | I am the person behind the judgment, not just a model or dashboard. | Short background, working principles, and what I will and will not claim. | Return to the case study or contact me. |
| Contact | A conversation is the next useful step. | One direct contact method and a specific invitation. | Send a message. |

**Deliberately omitted:** a separate blog, services page, resume page, testimonials page, and gallery. They do not currently prove the claim or improve the one action; they can be added only when real evidence gives them a job.

The companion visual sketch is [portfolio_sitemap_sketch.svg](portfolio_sitemap_sketch.svg). It is a clean digital version of the sketch to photograph or screenshot for submission.

## 2. Claude Project configuration

**Project name:** `FlyRank Content Archetype Portfolio`

Paste these custom instructions into the Project:

> I am an ML internship learner building a small portfolio around the FlyRank content-archetype project. My proof statement is: "I use observable page structure to organize a large content inventory into interpretable archetypes that help editors compare like with like. The work is descriptive decision support, not proof that a cluster causes better search performance."
>
> Act as a patient tutor and rigorous portfolio editor. Use this voice card as a standing instruction: direct, warm, plain, specific, evidence-led. Use this visual identity as a standing build instruction: DM Sans for headings, body text, labels, and buttons; IBM Plex Mono only for code, measured values, and compact metadata; `#17201D` near-black text, `#F8F7F2` warm white, `#145C52` deep green, and `#E3A84B` as the only accent. Keep the mood calm, precise, and editorial so the analysis, numbers, and screenshots remain the most memorable part of the portfolio. Explain reasoning in plain language, ask one useful clarifying question when the brief is ambiguous, and help me learn rather than silently taking over. Pressure-test whether each page, claim, chart, and call to action supports the proof statement. Flag unsupported causal language, missing evidence, privacy risks, and unnecessary scope. Prefer concise, specific feedback with an actionable next step. Never invent metrics, clients, screenshots, account setup, or personal experience. Preserve my judgment over the research question, ethical boundaries, and final wording.

## 3. Real pressure-test prompt

Run this prompt inside the configured Claude Project and save the response with a screenshot:

> Pressure-test this portfolio sitemap against my proof statement and one action. The audience is a content lead or hiring reviewer. The proof statement is: "I use observable page structure to organize a large content inventory into interpretable archetypes that help editors compare like with like. The work is descriptive decision support, not proof that a cluster causes better search performance." The one action is: "Open the case study, then contact me to discuss a similar content-analysis problem."
>
> Sitemap: Landing -> Work/Case Study -> About -> Contact. Landing states the claim and shows one measured finding. Work explains question, data, method, evidence, limits, and decision use. About explains who I am and my working principles. Contact offers one direct way to start a conversation.
>
> Tell me: (1) the strongest part of this path, (2) the biggest break between the claim and the action, (3) one page or section to remove, (4) one section to add or rewrite, and (5) the exact change you recommend. Be skeptical, specific, and do not invent evidence.

### Saved pressure-test response

**Status:** Pending execution in the user's Claude Project. This section must contain the verbatim Claude response before submission; the repository cannot authenticate the user's Claude account or generate a genuine Claude screenshot.

**Change to record after running it:** Choose at least one concrete revision from Claude's response, for example tightening the landing-page finding so it shows a measured result and adding a visible case-study-to-contact invitation after the limitations section. Record the actual change made, not a generic promise.

## 4. Evidence checklist

| Requirement | Status | Evidence |
|---|---|---|
| Sitemap sketch | Draft ready | Photograph or screenshot of the hand-drawn sketch, or screenshot of the companion visual sketch. |
| Claude account | User action required | Signed-in Claude screenshot. |
| ChatGPT account | User action required | Signed-in ChatGPT screenshot. |
| Gemini account | User action required | Signed-in Gemini screenshot. |
| Perplexity account | User action required | Signed-in Perplexity screenshot. |
| Claude Project with genuine instructions | Instructions ready; account evidence pending | Project overview and custom-instructions screenshots. |
| Real Claude pressure test | Prompt ready; response evidence pending | Screenshot showing the prompt and complete output, plus the recorded sitemap change. |