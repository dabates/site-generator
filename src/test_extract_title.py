import unittest

from src.markdown_blocks import extract_title


class ExtractTitleTests(unittest.TestCase):
    def test_extract_title(self):
        markdown = """# Test Markdown Title

This is a paragraph text block"""

        title = extract_title(markdown)

        self.assertEqual(title, "Test Markdown Title")

    def test_extract_title_with_extra_spaces(self):
        markdown = "#   Hello   "
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_first_h1_only(self):
        markdown = """# First Title

# Second Title
"""
        self.assertEqual(extract_title(markdown), "First Title")

    def test_ignore_h2_and_lower_headings(self):
        markdown = """## Not a Title
### Also not a Title
"""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("Could not extract title", str(context.exception))

    def test_extract_title_with_inline_markdown(self):
        markdown = "# **Bold Title**"
        self.assertEqual(extract_title(markdown), "**Bold Title**")

    def test_extract_title_from_multiline_markdown(self):
        markdown = """# Main Title

This is a paragraph with **bold** text.

## Subheading
"""
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_extract_title_no_h1_should_raise_exception(self):
        markdown = "This is just a paragraph."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("Could not extract title", str(context.exception))

    def test_extract_title_empty_string_should_raise_exception(self):
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("Could not extract title", str(context.exception))

    def test_extract_title_h1_without_space_should_not_be_extracted(self):
        markdown = "#Hello"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("Could not extract title", str(context.exception))


if __name__ == '__main__':
    unittest.main()
