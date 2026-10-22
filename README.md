# ctf-notes

Writeups for CTF challenges I solve

> 🚧 **Status: planning** — architecture and README first, code next.

## Why

Solving CTFs is how security skills stay sharp; writing them up is how they stay yours. Every challenge gets a structured writeup: recon, exploit, lessons — honest about what I got wrong.

## Planned features

- Organized by category: web, crypto, pwn, forensics, misc
- Standard writeup template: summary → recon → solve → lessons
- Working exploit code with comments
- A progress log of platforms (picoCTF, HTB, etc.)

## Stack

`python` `pwntools` `ghidra`

## Notes

No flags of active HTB machines are published — retired boxes only, per the rules.

## License

MIT, see [LICENSE](LICENSE).


## Writeup format

each challenge gets the prompt, tools used, solve path (including dead ends), and a takeaway. Keep the steps reproducible and explain why the approach worked.

Use this template for new notes:

```text
# Challenge name
Category: web | crypto | pwn | forensics | reversing | misc
Platform / event:
Difficulty:

## Summary
## Recon
## Solve
## Dead ends
## Takeaway
```

## Tooling

pwntools for pwn, ghidra for reversing, wireshark for the wire, burp for web. every writeup starts from the same template: prompt, recon, dead ends, solve, takeaway.

## Reading order

start with the web writeups (gentlest ramp), then crypto, then pwn — each assumes the previous. reversing entries stand alone; read them whenever.

## Workflow

notes during the solve, writeup within 48 hours while the dead ends still sting.

## History

the first notes were from a 2022 college CTF where the author solved nothing and learned everything. the writeups since are the compound interest on that weekend.


## Maintenance notes

A reproducible writeup should record scope, tools and versions, assumptions, failed approaches, root cause, and lessons learned. Confirm publication is allowed, sanitize target details, and never include secrets from real environments.
