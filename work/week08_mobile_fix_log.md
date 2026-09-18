# Mobile and Readability Fix Log

## Before

- The public page had a clean single-column layout, but the profile note incorrectly said the
  LinkedIn link was still a placeholder.
- Text links were ordinary inline links with no minimum touch area. They worked with a mouse, but
  they were less comfortable to tap on a phone.
- Form controls were readable, but the submit button had no explicit 44px minimum target and links,
  inputs, and buttons had no visible keyboard focus treatment.
- The page had no captured work images to compress; the only image is the small local favicon.

## Changes

- Kept the one-column layout and verified it at a 390px viewport. The browser audit reported no
  horizontal overflow; form fields fit inside the content column.
- Changed the profile labels to `Request CV by email` and `Book by email`, which describes the
  actual behavior instead of implying that direct assets already exist.
- Gave profile links and the submit button a minimum 44px height for more reliable touch use.
- Added a visible amber `:focus-visible` outline to links, inputs, the textarea, and the button.
- Kept body text at 18px with 1.6 line height and the existing readable DM Sans / IBM Plex Mono
  identity system.
- Confirmed the favicon uses a relative path and remains small; no oversized portfolio images exist
  in the published `docs/` folder.

## Verification

- Source diagnostics pass for `docs/index.html`.
- Narrow browser audit at 390px: no horizontal overflow; form controls fit; all six links expose
  valid destinations; the form has one HTTPS POST action.
- A real-phone check is still required: open the public URL on a physical phone after pushing the
  changes, tap every link, and capture the before/after evidence. This browser viewport is not a
  substitute for that device check.