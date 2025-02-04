import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf_node = LeafNode("p", "This is a paragraph of text")
        html_node2 = LeafNode("p", "This is a paragraph of text")

        self.assertEqual(leaf_node, html_node2)

    def test_print(self):
        leaf_node = LeafNode("p", "This is a paragraph of text")
        self.assertEqual(str(leaf_node), "LeafNode(tag=\"p\", value=\"This is a paragraph of text\")")

    def test_print_withprops(self):
        leaf_node = LeafNode("p", "This is a paragraph of text", {"title": "test"})
        self.assertEqual(str(leaf_node), "LeafNode(tag=\"p\", value=\"This is a paragraph of text\", props=\"{'title': 'test'}\")")

    def test_notag(self):
        leaf_node = LeafNode(None, "This is a paragraph of text")
        self.assertEqual(leaf_node.to_html(), 'This is a paragraph of text')

    def test_tag(self):
        leaf_node = LeafNode("p", "This is a paragraph of text")
        self.assertEqual(leaf_node.to_html(), '<p>This is a paragraph of text</p>')

    def test_btag(self):
        leaf_node = LeafNode("b", "Bold text")
        self.assertEqual(leaf_node.to_html(), '<b>Bold text</b>')


if __name__ == "__main__":
    unittest.main()
