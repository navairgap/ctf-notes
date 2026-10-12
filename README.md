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

---
maintained · verified 2026-09-30
---
maintained · verified 2026-10-01
---
maintained · verified 2026-10-02

## Writeup format

each challenge gets: the prompt, tools used, the solve path with dead ends included, and a takeaway line. dead ends matter — they're where the learning lives. PRs in this shape are welcome.

## Writeup format

each challenge gets: the prompt, tools used, the solve path with dead ends included, and a takeaway line. dead ends matter — they're where the learning lives. PRs in this shape are welcome.

## Tooling

pwntools for pwn, ghidra for reversing, wireshark for the wire, burp for web. every writeup starts from the same template: prompt, recon, dead ends, solve, takeaway.
