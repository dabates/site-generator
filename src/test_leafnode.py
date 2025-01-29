import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf_node = LeafNode("p", "This is a paragraph of text")
        html_node2 = LeafNode("p", "This is a paragraph of text")

        self.assertEqual(leaf_node, html_node2)

    def test_notag(self):
        leaf_node = LeafNode(None, "This is a paragraph of text")
        self.assertEqual(leaf_node.to_html(), 'This is a paragraph of text')

    def test_tag(self):
        leaf_node = LeafNode("p", "This is a paragraph of text")
        with self.assertRaises(NotImplementedError):
            leaf_node.to_html()


if __name__ == "__main__":
    unittest.main()
