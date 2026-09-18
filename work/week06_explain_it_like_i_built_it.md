# Week 6 - Explain It Like I Built It

## How my empty portfolio page is put together

The part I chose to understand is how my blank portfolio page turns into something a browser can
display. I used to think a web page was one block that CSS somehow “designed.” I now understand it
as two layers working together: HTML describes what the page contains, and CSS describes how those
things should look and sit on the screen.

In my real file, `docs/index.html`, the outer structure starts with `html`, then `head` and `body`.
The `head` is information for the browser rather than content I want visitors to read. It says the
document uses modern HTML, sets the mobile viewport, gives the page a title, loads the favicon, and
loads the two font families from Google Fonts. The `body` contains the visible portfolio.

Inside the body I use one `main` element. That is the page’s main content area, and it contains the
monogram image, a small eyebrow label, my name as the `h1`, the one-line claim, a decorative rule,
two paragraphs, and a footer. The order matters. The `h1` is the main heading, so a visitor and a
screen reader can understand the page hierarchy. The link is ordinary HTML too: its `href` points
to the public GitHub version of my identity notes, so clicking it does not require JavaScript.

The CSS starts with variables in `:root`. For example, `--ink` stores the dark text color and
`--paper` stores the warm background. If I change a color later, I can change the variable once
instead of searching through every rule. The `main` rule uses `width: min(720px, calc(100% - 40px))`.
In plain words, the content can never grow wider than 720 pixels, but on a small phone it leaves
20 pixels of breathing room on each side. That is why the same simple page can work on a laptop and
a phone without a separate mobile page.

The `clamp()` value on the heading makes the type responsive within a minimum and maximum size. The
layout changes size, but it does not change the content or require a framework. The `.eyebrow`,
`.claim`, `.rule`, and `footer` selectors target reusable classes. A class is a label I give an HTML
element so CSS can style that kind of element consistently.

The image paths taught me an important deployment lesson. The favicon used to point up to
`../work/portfolio-favicon.svg`. That worked only when the whole repository was available. GitHub
Pages publishes the `docs` folder as the site, so the deployed page needs the asset inside that
published folder. I copied the favicon to `docs/portfolio-favicon.svg` and changed the image and
icon paths to `portfolio-favicon.svg`. Relative paths mean “look next to this page,” which makes the
asset available in the published site.

I can now explain this page without saying that an AI magically built it. HTML gives the browser
the content and hierarchy. CSS gives that content its spacing, colors, fonts, and responsive limits.
The asset files must live where the host can publish them, and links must point to places a visitor
can actually reach. That is the piece I now own well enough to edit and teach to a friend.