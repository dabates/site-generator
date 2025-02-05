import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_create_html_node_tag(self):
        node = HtmlNode(tag="p")

        self.assertEqual(node.tag, "p")

    def test_create_html_node_value(self):
        node = HtmlNode(value="Hello")

        self.assertEqual(node.value, "Hello")

    def test_create_html_node_children(self):
        child = HtmlNode(tag="b", value="Bold")
        node = HtmlNode(tag="p", children=[child])

        self.assertEqual(node.children, [child])

    def test_create_html_node_props(self):
        node = HtmlNode(props={"href": "http://google.com"})

        self.assertEqual(node.props, {"href": "http://google.com"})

    def test_eq_same_objects(self):
        node1 = HtmlNode(tag="p", value="Hello, World")
        node2 = HtmlNode(tag="p", value="Hello, World")

        self.assertEqual(node1, node2)

    def test_eq_different_objects(self):
        node1 = HtmlNode(tag="p", value="Hello")
        node2 = HtmlNode(tag="p", value="World")

        self.assertNotEqual(node1, node2)

    def test_props_to_html_with_props(self):
        node = HtmlNode(props={"href": "http://localhost", "target": "_blank"})

        self.assertEqual(node.props_to_html(), ' href="http://localhost" target="_blank"')

    def test_props_to_html_no_props(self):
        node = HtmlNode(tag="p", value="Test")

        self.assertEqual(node.props_to_html(), "")

    def test_repr_with_props(self):
        node = HtmlNode(props={"href": "http://localhost", "target": "_blank"})
        expected_repr = 'HtmlNode(props="{\'href\': \'http://localhost\', \'target\': \'_blank\'}")'

        self.assertEqual(repr(node), expected_repr)

    def test_repr_without_props(self):
        node = HtmlNode(tag="p", value="Hello")
        expected_repr = 'HtmlNode(tag="p", value="Hello")'

        self.assertEqual(repr(node), expected_repr)

    def test_to_html_basic(self):
        node = HtmlNode(tag="p", value="Hello")

        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_to_html_with_children(self):
        child1 = HtmlNode(tag="b", value="Bold")
        child2 = HtmlNode(tag="i", value="Italic")
        parent = HtmlNode(tag="p", children=[child1, child2])

        self.assertEqual(parent.to_html(), "<p><b>Bold</b><i>Italic</i></p>")

    def test_to_html_with_props(self):
        node = HtmlNode(tag="a", value="Click Here", props={"href": "http://disney.com", "target": "_blank"})

        self.assertEqual(node.to_html(), '<a href="http://disney.com" target="_blank">Click Here</a>')

    def test_to_html_with_value(self):
        node = HtmlNode(tag="p", value="Hello")

        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_to_html_with_value_and_children(self):
        child = HtmlNode(tag="b", value="Bold")
        node = HtmlNode(tag="p", value="Hello ", children=[child])

        self.assertEqual(node.to_html(), "<p>Hello <b>Bold</b></p>")

    def test_to_html_with_empty_value_and_children(self):
        child = HtmlNode(tag="b", value="Bold")
        node = HtmlNode(tag="p", value="", children=[child])

        self.assertEqual(node.to_html(), "<p><b>Bold</b></p>")


if __name__ == "__main__":
    unittest.main()
