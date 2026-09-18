# Week 4 - Stack Decision

## My constraints

I want free tools only. My honest skill level is beginner-to-intermediate: I am comfortable
with Python notebooks and learning basic HTML and CSS, but I do not want to spend this
assignment learning a full frontend framework or maintaining a server.

My portfolio needs to move a skeptical content lead from one clear claim to one action:
read the FlyRank case study, then contact me about a similar content-inventory problem. The
sitemap is `Landing -> Work / Case Study -> About -> Contact`. The landing page will show the
claim and one measured finding. The case study will show the question, data scope, method,
evidence, limitations, and decision use. About will explain who I am and my working principles.
Contact will offer one direct way to start a conversation.

The work must be shown as readable long-form case-study writing, notebook or repository links,
legible charts and screenshots, and eventually an embedded or linked analysis demo if one is
useful. Nothing needs to be dynamic at launch. I do not need accounts, a database, login, or a
backend yet.

## Three options

### 1. Plain HTML and CSS on GitHub Pages

I would write the pages directly in HTML and CSS, keep the assets in the repository, and publish
the `docs/` folder from the `main` branch with GitHub Pages. The repository would hold both the
site and the analysis evidence.

- Free host: GitHub Pages
- Backend: Not yet; a mailto link is enough for the first version
- Strength: Best fit for readable case studies, charts, screenshots, and public notebook/repo links
- Trade-off: I must make layout and responsive styling decisions myself, and a contact form would
  need a third-party service later

### 2. No-code portfolio on Carrd or Framer

I would assemble the four-page structure in a visual builder, upload selected images, and link out
to the repository and notebooks.

- Free host: Carrd or Framer free tier, where the chosen features and URL are available
- Backend: Not yet; the first version could use an email link
- Strength: Fast visual editing and easy spacing/layout changes
- Trade-off: Free-tier limits, less control over evidence-heavy long-form pages, and another tool
  to learn and maintain

### 3. React or Next.js portfolio on Vercel

I would build reusable components for the landing page, case study, About, and Contact pages,
then deploy from GitHub with a modern frontend workflow.

- Free host: Vercel Hobby
- Backend: Not yet; static rendering is enough at launch
- Strength: Strongest path if the site grows into interactive charts, an embedded demo, or richer
  filtering and navigation
- Trade-off: Dependency upgrades, build configuration, framework concepts, and deployment debugging
  would consume time that should go into the evidence

## Pressure test of the front-runner

I choose plain HTML and CSS on GitHub Pages. If I pick the simplest option, the main thing that
breaks is convenience: I will not get a visual editor or built-in contact form, and I will need to
check mobile spacing and relative asset paths myself. That is acceptable because the first version
only needs a clear case study, charts, screenshots, and links.

If I pick the most powerful option, I maintain a package manifest, framework conventions, build
errors, dependency updates, and a deployment pipeline. I could finish a basic version in two weeks,
but the extra machinery would reduce the time available to validate and explain the actual ML work.

The simplest option shows my work well because the important proof is text, images, charts, and
links rather than application state. GitHub also keeps the code, notebooks, and portfolio close
together. I can add a static chart or a linked notebook now and add an interactive demo later if
the evidence earns one.

## Decision in my own words

I chose plain HTML and CSS hosted on GitHub Pages. It is free, matches my current skill level,
and is enough for the portfolio I actually need: calm, readable pages that make the FlyRank
analysis inspectable. It also keeps the site and the analysis repository together, which makes the
case study easier to trust and update.

I did not choose Carrd or Framer because their visual editing would be convenient, but the free
setup gives me less control over long-form evidence and adds a separate system around work that
already lives in GitHub. I did not choose React or Next.js because the interactive benefits are
not needed yet and the maintenance cost is higher. **Can I maintain this?** Yes: I can edit HTML,
CSS, images, and links directly, and GitHub Pages removes server maintenance. **Does it show my
work well?** Yes: it supports readable case studies, real chart crops, notebook links, repository
links, and a later static demo without pretending that a backend exists.