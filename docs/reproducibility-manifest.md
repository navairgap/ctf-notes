# CTF writeup reproducibility manifest

A reproducibility manifest records enough context for a reader to understand and repeat an authorized challenge workflow without exposing secrets or depending on the author's machine.

## Suggested fields

- Challenge title, category, platform/event, and release or retirement status.
- Date the challenge was solved and the date the writeup was published.
- Operating system or disposable lab image identifier.
- Tool names and versions, including relevant compiler or interpreter versions.
- Input artifact names and cryptographic hashes when the challenge permits distributing them.
- Exact commands or scripts used, with sensitive values replaced by invalid placeholders.
- Expected output characteristics and the reasoning used to interpret them.
- Known limitations, assumptions, and steps that could not be reproduced.

## Environment isolation

Prefer a disposable VM or container with no personal credentials mounted. Keep challenge artifacts separate from personal files. Do not embed VPN configuration, browser profiles, SSH keys, cloud credentials, or tokens in the manifest.

## Reproducibility and honesty

Distinguish a verified reproduction from a description based on memory. Record unavailable downloads or changed platform behavior rather than inventing a replacement artifact. A hash identifies the bytes tested; it does not grant permission to redistribute those bytes.

## Review

Check that every published command is within the authorized challenge scope, every linked artifact is permitted for release, and all output is sanitized. A reader should be able to identify which steps are deterministic and which depend on a platform or environment that may have changed.