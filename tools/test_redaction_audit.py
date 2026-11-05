import tempfile
import unittest
from pathlib import Path

from redaction_audit import Finding, scan_file, scan_tree


class RedactionAuditTests(unittest.TestCase):
    def test_reports_rule_and_line_without_returning_secret_value(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            token = "ghp_" + "A" * 28
            source = root / "writeup.md"
            source.write_text(
                "safe example\n"
                + "token = " + token + "\n"
                + "Authorization: Bearer " + "b" * 32 + "\n",
                encoding="utf-8",
            )
            findings = scan_file(source, root)
            self.assertEqual(
                findings,
                [
                    Finding("writeup.md", 2, "github-token"),
                    Finding("writeup.md", 3, "bearer-authorization"),
                    Finding("writeup.md", 2, "credential-assignment"),
                ],
            )
            rendered = repr(findings)
            self.assertNotIn(token, rendered)
            self.assertNotIn("b" * 32, rendered)

    def test_detects_private_key_marker_and_aws_key_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "notes.txt"
            source.write_text(
                "-----BEGIN OPENSSH PRIVATE KEY-----\n"
                "AKIA" + "A" * 16 + "\n",
                encoding="utf-8",
            )
            rules = {item.rule for item in scan_file(source, root)}
            self.assertIn("private-key-marker", rules)
            self.assertIn("aws-access-key-id", rules)

    def test_ignores_explicit_placeholders(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "example.md"
            source.write_text(
                "secret = REPLACE_ME_LONG\n"
                "api_key = YOUR_TOKEN_HERE\n"
                "access_token = dummy-secret\n",
                encoding="utf-8",
            )
            self.assertEqual(scan_file(source, root), [])

    def test_skips_binary_oversized_and_symlinked_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / "binary.dat"
            binary.write_bytes(b"secret = " + b"x" * 24 + b"\0")
            huge = root / "large.txt"
            huge.write_text("x" * 128, encoding="utf-8")
            outside = root.parent / (root.name + "-outside.txt")
            outside.write_text("ghp_" + "B" * 28, encoding="utf-8")
            link = root / "outside-link.txt"
            try:
                link.symlink_to(outside)
            except (NotImplementedError, OSError) as exc:
                self.skipTest(f"symlink unavailable: {exc}")
            self.assertEqual(scan_file(binary, root), [])
            self.assertEqual(scan_file(huge, root, max_bytes=32), [])
            self.assertEqual(scan_file(link, root), [])
            outside.unlink()

    def test_tree_scan_prunes_dependency_and_git_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".git").mkdir()
            (root / ".git" / "secret.txt").write_text("ghp_" + "C" * 28)
            (root / "notes.md").write_text("safe notes")
            self.assertEqual(scan_tree(root), [])


if __name__ == "__main__":
    unittest.main()
