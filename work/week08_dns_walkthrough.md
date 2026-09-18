# DNS Walkthrough

DNS is the internet's address book. People use a name such as `himanshusharma-2856.github.io`
because it is easier to remember than an IP address. Computers still need an IP address, so DNS
translates the name into the network address of the service hosting the site.

When someone types the site address, the browser first checks information it already knows, such as
its own cache. If it does not have an answer, the request goes to a **recursive resolver**, usually
operated by the internet provider, a company, or a public DNS service. The resolver looks for the
answer on the user's behalf. It asks the domain's **nameserver**, which is the authoritative service
that stores the DNS records for that domain. The resolver saves the answer for the record's TTL, or
time to live, so the next request can be faster.

The nameserver returns a record. An `A` record maps a name directly to an IPv4 address. An `AAAA`
record does the same for IPv6. A **CNAME** record maps one hostname to another hostname. For example,
if I owned `www.himanshusharma.com`, I could create a CNAME from `www.himanshusharma.com` to a host
name supplied by my hosting provider. The resolver follows that name until it gets the address needed
to connect. A CNAME is an alias for a hostname, not a place to type an IP address, and it normally
cannot be used at the root of a domain in the same way as an A record.

After DNS gives the browser the host address, the browser opens a connection and requests the page.
For an HTTPS site, the host also presents a TLS certificate proving that the request is for the
correct domain and encrypting the connection. The hosting service then returns `index.html` and its
relative assets, such as the favicon. DNS does not contain the page itself; it only helps the browser
find the service that can answer.

For this project, the free-host path is GitHub Pages. The repository contains `docs/index.html`, and
the Pages workflow publishes that folder. The public GitHub Pages hostname is controlled by GitHub,
so I do not need to create DNS records for the default URL. If I later buy a custom domain, I would
add the custom-domain setting in GitHub Pages and create the DNS record at my domain registrar. I
would follow GitHub's exact target hostname rather than guessing it, wait for DNS propagation, then
test the address in a private browser window over HTTPS.

In short: the browser asks a resolver, the resolver consults the authoritative nameserver, the
nameserver returns a record such as an A or CNAME, and the browser uses the result to reach the host.
The host answers the HTTPS request with the site files. DNS is the routing step between a human-friendly
name and the server that delivers the page.