import unittest

from src.text_utils import split_nodes_image
from src.textnode import TextNode, TextType


class SplitNodesImage(unittest.TestCase):
    def test_split_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.NORMAL)
        new_nodes = split_nodes_image([node])

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
        ])

    def test_split_multiple_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![nothing](https://nothing.com/nope.gif)",
            TextType.NORMAL)
        new_nodes = split_nodes_image([node])

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
            TextNode(" and ", TextType.NORMAL),
            TextNode("nothing", TextType.IMAGE, 'https://nothing.com/nope.gif'),
        ])

    def test_split_multiple_image_nodex(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.NORMAL)
        node2 = TextNode("This is text with a ![nothing](https://nothing.com/nope.gif)", TextType.NORMAL)
        new_nodes = split_nodes_image([node, node2])

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("nothing", TextType.IMAGE, 'https://nothing.com/nope.gif'),
        ])

    def test_split_no_image(self):
        node = TextNode("This is text with a no images", TextType.NORMAL)
        new_nodes = split_nodes_image([node])

        self.assertEqual(new_nodes, [
            TextNode("This is text with a no images", TextType.NORMAL),
        ])


if __name__ == '__main__':
    unittest.main()
