# Week 3 - Portfolio Visual Identity and Image Curation

**Portfolio:** FlyRank content-archetype analysis  
**Audience:** A content operations lead at an SEO or content agency managing a large page portfolio  
**One action:** Email me to discuss a similar content-inventory problem

## One-line claim

**I turn page structure into a clearer, evidence-led review queue.**

This is short enough to remember and specific enough to test. It does not promise better rankings or pretend that the clustering work replaces editorial judgment.

## Content map

Every page moves the same reader toward the same action: email me about a similar content-inventory problem.

| Page | Sections in order | Case placement | Named CTA | Proof still needed |
|---|---|---|---|---|
| Landing | Claim -> measured structural contrast -> short explanation of the decision -> selected work link | Lead with FlyRank content-archetype analysis | Read the case study | Final deployed landing URL and one clean chart crop |
| Work / Case Study | Problem -> data scope -> method and decisions -> evidence -> limitations -> human review step | Lead case: FlyRank content-archetype analysis | Email me to discuss a similar problem | Executed notebook link, final cluster/profile output, and one legible evidence capture |
| About | Who I am -> working principles -> what I will and will not claim | No separate case; point back to the lead case | Return to the case study or email me | Final short bio and real headshot if an About photo is used |
| Contact | Specific invitation -> email address -> privacy-safe note | No case needed | Email me | Confirm the email link works on the deployed page |

**Deliberately omitted:** blog, services page, testimonials, gallery, and a resume page. They do not currently add proof for this claim or improve the one action.

## Identity kit

### Type

- **Headings:** [DM Sans](https://fonts.google.com/specimen/DM+Sans), 700 weight.
- **Body and labels:** DM Sans, 400 and 500 weights.
- **Code and metric values:** [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono), 400 and 600 weights.

Using one primary family keeps the portfolio consistent. The mono face is reserved for evidence values and code, where it has a real job.

### Palette

| Role | Hex | Use |
|---|---|---|
| Near-black text | `#17201D` | Headings, body text, dark panels |
| Warm white | `#F8F7F2` | Page background and quiet sections |
| Main green | `#145C52` | Links, rules, selected states |
| Single accent | `#E3A84B` | Small evidence highlights and attention markers only |

The palette is deliberately small. Teal signals the path through the evidence; amber is reserved for a result or caveat that deserves a second look. The work remains the most colorful thing on the page.

### Logo / favicon

The favicon is a simple `FR` mark in the main green. It is legible at small size, contains no decorative claim, and does not compete with a chart or case-study title.

Asset: [portfolio-favicon.svg](portfolio-favicon.svg)

### Two-line style note

DM Sans on warm white with near-black text, deep green links, and one restrained amber accent. The mood is calm, precise, and editorial: generous space and clear evidence framing let the analysis, numbers, and screenshots do the memorable work.

### Reusable build note

Use DM Sans for every heading, paragraph, label, and button. Use IBM Plex Mono only for code, measured values, and compact metadata. Keep body text near `18px`, line height near `1.6`, section spacing generous, and accents rare. Never add a decorative gradient, a second accent color, or a background image that competes with the evidence.

## Image curation

### Final image set

| Image | Role | Decision | Why it serves the proof |
|---|---|---|---|
| `outputs/charts/top_feature_importance.svg` | Work page evidence | Keep, after a clean crop and readable caption | It shows which measured inputs mattered to the refresh model and keeps the work inspectable. |
| `outputs/charts/action_mix.svg` | Work page evidence | Keep, after checking labels at mobile width | It connects analysis to the reviewer-facing action categories without pretending the model makes the editorial decision. |
| `outputs/charts/confidence_mix.svg` | Work page evidence | Keep if the case study discusses confidence; otherwise omit | It supports the distinction between a review aid and an automatic rewrite instruction. |
| Executed `w03_data_contract.ipynb` query output | Work page evidence | Keep as a cropped screenshot or rendered table | It proves the row grain, March scope, availability filter, and leakage check from the actual warehouse work. |
| Executed `w01_research_question.ipynb` structural comparison output | Landing or Work evidence | Keep as a clean table crop | It gives the visitor one measured contrast before asking them to read the full case. |
| Real portrait, if used | About | Use a real photo only | A generated portrait would misrepresent the person behind the judgment. |

**Image rule:** screenshots of the work are evidence, not decoration. Crop away browser chrome, keep labels legible, redact anything private, and write one sentence below each image explaining what a stranger should notice.

### Generated connective-tissue options

I do not need a generated hero image for this portfolio. If a visual separator is useful, the only acceptable generated direction is a quiet editorial texture: flat paper grain, soft off-white field, one deep-green line, and no objects, faces, fake dashboards, or glowing AI motifs. Keep every generated asset in that same restrained style and use it only between sections.

### Rejection note

I rejected the common generated “AI analytics” hero: a glowing dashboard floating over a dark gradient with abstract data streams. It is polished at a glance but fails the proof. It makes the site memorable instead of the analysis, implies a product that does not exist, and gives the visitor no evidence they can inspect. A clean crop of the real feature-importance chart is less dramatic and more trustworthy, so it wins.

## Decision record

The identity is ready to hand to a stranger: one claim, one action, four pages with ordered content, one type family plus a functional mono face, four colors, a favicon, and a real-capture-first image set. The remaining proof items are marked rather than invented; they must be gathered when the notebook and portfolio page are actually deployed.