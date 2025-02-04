import unittest

from src.htmlnode import HtmlNode
from src.leafnode import LeafNode
from src.markdown_blocks import markdown_to_html_node


class MarkdownToHtmlTests(unittest.TestCase):
    def test_markdown_to_html(self):
        markdown = """# Header Level 1

Paragraph text

- List Item 1
- List Item 2

[link](http://google.com)

*Italic* text

**Bold** text

```Code block```

> Quoted string

1. OrderedList Item 1
2. OrderedList Item 2
"""
        nodes = markdown_to_html_node(markdown)

        self.assertEqual(nodes, HtmlNode("div", children=[
            # Header
            HtmlNode("h1", children=[
                LeafNode(None, "Header Level 1", )
            ]),
            # Paragraph
            HtmlNode("p", children=[
                LeafNode(None, value="Paragraph text")
            ]),
            # Unordered List
            HtmlNode("ul", children=[
                HtmlNode("li", children=[
                    LeafNode(None, value="List Item 1")
                ]),
                HtmlNode("li", children=[
                    LeafNode(None, value="List Item 2")
                ])
            ]),
            # Link
            HtmlNode("p", children=[
                LeafNode("a", value="link", props={
                    'href': 'http://google.com'
                })
            ]),
            # Italic
            HtmlNode("p", children=[
                LeafNode("i", value="Italic"),
                LeafNode(None, value=" text")
            ]),
            # Bold
            HtmlNode("p", children=[
                LeafNode("b", value="Bold"),
                LeafNode(None, value=" text")
            ]),
            # Code
            HtmlNode("pre", children=[
                HtmlNode("code", children=[
                    LeafNode(None, value="Code block")
                ])
            ]),
            # Quoted String
            HtmlNode("blockquote", children=[
                LeafNode(None, value="Quoted string")
            ]),
            # Ordered List
            HtmlNode("ol", children=[
                HtmlNode("li", children=[
                    LeafNode(None, value="OrderedList Item 1")
                ]),
                HtmlNode("li", children=[
                    LeafNode(None, value="OrderedList Item 2")
                ])
            ])
        ]),
                         )


if __name__ == '__main__':
    unittest.main()
