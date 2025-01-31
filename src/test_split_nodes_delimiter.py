import unittest

from src.split_nodes import split_nodes_delimiter
from src.textnode import TextNode, TextType


class SplitNodesDelimiter(unittest.TestCase):
    def test_split_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL)
        ])

    def test_split_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL)
        ])

    def test_split_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL)
        ])

    def test_split_code_block_error(self):
        node = TextNode("This is text with a `code block word", TextType.NORMAL)

        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == '__main__':
    unittest.main()
