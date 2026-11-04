# Challenge archive handling checklist

Challenge archives, disk images, and binaries are untrusted inputs even when they come from an official platform. Inspect them in a disposable workspace before extracting or executing anything.

## Before extraction

- Record the download source, retrieval date, filename, byte size, and SHA-256 digest.
- List archive members without extracting them and inspect their file types.
- Reject absolute paths, parent-directory traversal, unexpected device nodes, and links that resolve outside the disposable extraction directory.
- Check for duplicate paths, case-folding collisions, and unexpectedly large expanded sizes.
- Keep the original archive read-only and perform analysis on a separate working copy.

## During analysis

- Extract only into a disposable VM or container with no personal credentials or sensitive host directories mounted.
- Do not run bundled installers or scripts merely to inspect an artifact.
- Keep network access disabled unless the challenge explicitly requires an authorized lab target.
- Preserve the original digest and record any transformations, unpacking tools, and tool versions.

## Before publishing

- Confirm the event permits redistributing the archive or derived artifacts. A hash is an identifier, not permission to redistribute.
- Remove credentials, private paths, hostnames, and unrelated metadata from logs and screenshots.
- Prefer synthetic or minimized fixtures when the original artifact contains unrelated personal or production data.
- State which steps were reproduced and which were only documented from memory.
