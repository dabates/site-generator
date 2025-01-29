import unittest

from src.leafnode import LeafNode
from src.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        p1 = ParentNode('p', [LeafNode("b", "bold")])
        p2 = ParentNode('p', [LeafNode("b", "bold")])

        self.assertEqual(p1, p2)

    def test_repr(self):
        p1 = ParentNode('p', [LeafNode("b", "bold")])
        self.assertEqual(str(p1), "ParentNode(p, [LeafNode(b, bold, None)], None)")

    def test_render(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    ## Test for errors
    def test_no_children(self):
        node = ParentNode('p', None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_tag(self):
        node = node = ParentNode(
            '',
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == '__main__':
    unittest.main()
