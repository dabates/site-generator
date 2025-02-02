import unittest

from src.markdown_blocks import block_to_block_type


class BlockToBlockType(unittest.TestCase):
    def test_heading(self):
        for i in range(1, 7):  # Test # to ######
            markdown = f"{'#' * i} Heading Text"
            self.assertEqual(block_to_block_type(markdown), "heading")

    def test_code_block(self):
        markdown = """```
    def hello():
        return "world"
    ```"""
        self.assertEqual(block_to_block_type(markdown), "code")

    def test_quote_block(self):
        markdown = """> This is a quote.
    > It spans multiple lines."""
        self.assertEqual(block_to_block_type(markdown), "quote")

    def test_unordered_list_asterisk(self):
        markdown = """* Item 1
    * Item 2
    * Item 3"""
        self.assertEqual(block_to_block_type(markdown), "unordered_list")

    def test_unordered_list_dash(self):
        markdown = """- Item A
    - Item B
    - Item C"""
        self.assertEqual(block_to_block_type(markdown), "unordered_list")

    def test_ordered_list(self):
        markdown = """1. First item
    2. Second item
    3. Third item"""
        self.assertEqual(block_to_block_type(markdown), "ordered_list")

    def test_ordered_list_wrong_numbering(self):
        markdown = """1. First item
    3. Wrong numbering
    5. Skipped numbers"""
        self.assertEqual(block_to_block_type(markdown), "paragraph")  # Should fall back to paragraph

    def test_mixed_unordered_and_ordered_list(self):
        markdown = """1. Ordered
    - Unordered
    3. Ordered"""
        self.assertEqual(block_to_block_type(markdown), "paragraph")  # Should be treated as a paragraph

    def test_paragraph(self):
        markdown = "This is just a paragraph. It contains text but no special formatting."
        self.assertEqual(block_to_block_type(markdown), "paragraph")


if __name__ == '__main__':
    unittest.main()
