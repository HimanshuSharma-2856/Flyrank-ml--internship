# One Dynamic Feature: Contact Form

I chose one feature for my portfolio: a contact form. The site is otherwise a static page. I chose
this because the portfolio's real next action is a conversation about a similar content-inventory
problem; a visitor should be able to send that message without opening a separate email program.

## What a backend is

A backend is the part of an application that runs away from the visitor's browser. It receives
requests, applies rules, stores or forwards data, and sends a response. My HTML and CSS are the
frontend: they display the form. GitHub Pages serves those files, but GitHub Pages does not process
form submissions or send email. That is why the form needs a separate backend service.

For this first version I use FormSubmit's free form endpoint as that service. I did not build a
custom server because this feature only needs one small action and a server would add maintenance,
credentials, and another place for mistakes. FormSubmit's first submission requires me to confirm my
email address, so the feature is not fully live until I submit a test message and click that
activation link.

## How the data flows

1. A visitor opens the GitHub Pages URL. The browser downloads `docs/index.html` and displays the
   form. No visitor data is sent just by opening the page.
2. The visitor enters a name, email address, and message. The browser checks that the required
   fields are present and that the email has an email-shaped value.
3. When the visitor clicks **Send message**, the browser sends an HTTPS `POST` request to the
   FormSubmit endpoint named in the form's `action` attribute. The request contains the three form
   fields plus a subject and a return URL.
4. FormSubmit receives the request, applies its own service rules, and forwards the message to my
   email address. On the first use, it sends an activation request that I must confirm.
5. FormSubmit redirects the browser to the GitHub Pages URL in `_next`. The message itself is in my
   email inbox, not stored by this repository.

This is a small but real frontend-to-service-to-email flow. The form does not pretend to be a
database, user account system, or AI feature. I will test it with a harmless message, confirm the
activation email if requested, check that the message reaches my inbox, and then verify that the
return page loads.

The main risks are spam, accidentally submitting sensitive information, and trusting a third-party
service without checking its current terms. The form therefore collects only the minimum three
fields, uses HTTPS, and shows a short explanation before submission. I will not ask visitors to
send passwords, private client data, or credentials. If the test message does not arrive, the honest
status is “not verified”; the presence of a form on the page is not proof that the feature works.