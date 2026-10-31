# CTF writeup publication and redaction checklist

A technically correct writeup can still violate challenge rules or expose information that should not be public. Review scope and publication permissions before sharing a solution.

## Authorization and timing

- Confirm the challenge platform or event permits publication of the solution.
- Respect event rules, embargoes, and active-machine policies.
- Do not publish flags, credentials, session cookies, private keys, or tokens from real environments unless the organizer explicitly requires a flag as proof and publication is allowed.
- Do not include steps that target infrastructure outside the challenge scope.
- For hosted labs, confirm whether the target is retired or explicitly released for writeup publication.

## Sanitization

Remove personal account identifiers, local filesystem paths, private hostnames, VPN addresses, API keys, browser cookies, and unrelated logs. Replace real credentials with clearly invalid placeholders. Inspect screenshots and terminal recordings as carefully as text; secrets can appear in window titles, shell prompts, browser bars, or environment output.

Do not use a production log as a fixture. Create synthetic examples that preserve the technical behavior without preserving unrelated user data.

## Technical quality

Record the challenge name/category, platform or event, date, tool versions, relevant assumptions, solve path, failed approaches, root cause, and lessons learned. Explain why each important step works rather than publishing a command transcript alone.

## Final review

Before publication, verify that the content is within scope, does not expose current targets, contains no live credentials, and accurately distinguishes observed facts from assumptions. When permission is unclear, do not publish the sensitive detail; ask the event organizer or omit it.