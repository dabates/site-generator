import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node2", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node), "TextNode(text=\"This is a text node\", text_type=\"bold\")")

    def test_normal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.text_node_to_html_node().to_html(), "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text_node_to_html_node().to_html(), "<b>This is a text node</b>")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text_node_to_html_node().to_html(), "<i>This is a text node</i>")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node.text_node_to_html_node().to_html(), "<code>This is a text node</code>")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, 'http://test.link/')
        self.assertEqual(node.text_node_to_html_node().to_html(), '<a href="http://test.link/">This is a text node</a>')

    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE,'http://img.link/a.jpg')
        self.assertEqual(node.text_node_to_html_node().to_html(), '<img src="http://img.link/a.jpg" alt="This is a text node"></img>')


if __name__ == "__main__":
    unittest.main()
