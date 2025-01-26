import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        html_node = HtmlNode(props={"href": "http://localhost", "target": "_blank"})
        html_node2 = HtmlNode(props={"href": "http://localhost", "target": "_blank"})

        self.assertEqual(html_node, html_node2)

    def test_neq(self):
        html_node = HtmlNode(props={"href": "http://localhost", "target": "_blank"})
        html_node2 = HtmlNode(props={"href": "http://localhost/here", "target": "newwin"})

        self.assertEqual(html_node, html_node2)

    def test_print(self) :
        html_node = HtmlNode(props={"href": "http://localhost", "target": "_blank"})
        output = f"{html_node}"
        self.assertIn("_blank", output)

    def test_props2html(self):
        html_node = HtmlNode(props={"href": "http://localhost", "target": "_blank"})
        output = html_node.props_to_html()
        self.assertEqual(' href="http://localhost" target="_blank"', output)

if __name__ == "__main__":
    unittest.main()
