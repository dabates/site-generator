import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "This is a paragraph of text")
        node2 = LeafNode("p", "This is a paragraph of text")

        self.assertEqual(node1, node2)

    def test_repr_no_props(self):
        node = LeafNode("p", "This is a paragraph")

        self.assertEqual(repr(node), 'LeafNode(tag="p", value="This is a paragraph")')

    def test_repr_with_props(self):
        node = LeafNode("p", "This is a paragraph", {"title": "test"})

        self.assertEqual(
            repr(node),
            'LeafNode(tag="p", value="This is a paragraph", props="{\'title\': \'test\'}")'
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Plain text")

        self.assertEqual(node.to_html(), "Plain text")

    def test_to_html_with_tag(self):
        node = LeafNode("p", "This is a paragraph")

        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_to_html_bold_tag(self):
        node = LeafNode("b", "Bold text")

        self.assertEqual(node.to_html(), "<b>Bold text</b>")

    def test_to_html_empty_value_with_tag(self):
        node = LeafNode("p", "")  # Empty string as value

        self.assertEqual(node.to_html(), "<p></p>")

    def test_to_html_no_value_raises_error(self):
        node = LeafNode("p", None)  # No value

        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
