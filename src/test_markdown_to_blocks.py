import unittest

from src.markdown_blocks import markdown_to_blocks


class MarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_block(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(blocks, [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ])

    def test_markdown_to_block_extra_spaces(self):
        markdown = """    # This is a heading    

 This is a paragraph of text. It has some **bold** and *italic* words inside of it.         

     * This is the first list item in a list block
* This is a list item
* This is another list item      """

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(blocks, [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ])

    def test_markdown_to_block_empty(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [''])

    def test_markdown_to_block_only_newlines(self):
        markdown = "\n\n\n\n"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [""])  # Should return a single empty block

    def test_markdown_to_block_multiple_blank_lines(self):
        markdown = """# Heading 1


This is a paragraph.


* List item 1
* List item 2


Another paragraph here.

"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [
            "# Heading 1",
            "This is a paragraph.",
            """* List item 1
* List item 2""",
            "Another paragraph here."
        ])

    def test_markdown_to_block_single_line(self):
        markdown = "# This is a heading"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ["# This is a heading"])

    def test_markdown_to_block_multiple_headings(self):
        """Test case with multiple headings separated by newlines."""
        markdown = """# Heading 1

# Heading 2

# Heading 3"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ["# Heading 1", "# Heading 2", "# Heading 3"])


if __name__ == '__main__':
    unittest.main()
