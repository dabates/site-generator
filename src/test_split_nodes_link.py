import unittest

from src.text_utils import split_nodes_link
from src.textnode import TextNode, TextType


class SplitNodesLink(unittest.TestCase):
    def test_split_link(self):
        node = TextNode("This is text with a [link](https://google.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, 'https://google.com'),
        ])

    def test_split_multiple_links(self):
        node = TextNode("This is text with a [link](https://google.com) and [link2](https://www.facebook.com)",
                        TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, 'https://google.com'),
            TextNode(" and ", TextType.TEXT),
            TextNode("link2", TextType.LINK, 'https://www.facebook.com'),
        ])

    def test_split_multiple_link_nodex(self):
        node = TextNode("This is text with a [link](https://google.com)", TextType.TEXT)
        node2 = TextNode("This is text with a [link2](https://www.facebook.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node, node2])

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, 'https://google.com'),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link2", TextType.LINK, 'https://www.facebook.com'),
        ])

    def test_split_no_link(self):
        node = TextNode("This is text with a no images", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertEqual(new_nodes, [
            TextNode("This is text with a no images", TextType.TEXT),
        ])


if __name__ == '__main__':
    unittest.main()
