# writeup safety

Before publishing, confirm the challenge is retired or publication is permitted. Do not include credentials, personal data, or secrets from real environments. Replace target addresses with placeholders unless disclosure is authorized. Explain root cause and reasoning, mark destructive commands, provide local reproduction where possible, include tool versions, and remove machine-specific paths. Respect platform rules about flags and spoilers.

## Final disclosure pass

Before committing a write-up, search the rendered text and attachments for API keys, session cookies, private target hostnames, personal data, and terminal output that contains credentials. Check that example commands target a local container or an authorized challenge instance and that destructive commands are labelled before execution. Record the challenge platform and retirement/publication status in the write-up so future readers can reassess whether disclosure is still appropriate.

## Reproducible artifacts

For each attached script, packet capture, or binary fixture, record its origin, purpose, size, and cryptographic hash. Identify tool versions and assumptions that affect the result. Prefer small synthetic fixtures over real-user or production data. Remove API keys, session cookies, private hostnames, and machine-specific paths from both text and metadata before publishing. Never include a live target's secrets just to make a reproduction more convenient.

## Handling downloaded artifacts

Treat challenge archives and binaries as untrusted. Record their source and hash, inspect file types before opening them, and analyze them in a disposable VM or container without host credentials or shared sensitive directories. Do not run an included install script merely to inspect the challenge. If a reproduction requires network access, restrict it to the explicitly authorized lab target and document that requirement.
