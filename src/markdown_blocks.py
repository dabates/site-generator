import re

from src.htmlnode import HtmlNode
from src.text_utils import text_to_textnodes
from src.textnode import TextType


def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.strip().split('\n\n'):
        blocks.append(block.strip())

    return blocks


def block_to_block_type(markdown):
    matches = re.findall(r"^```[\s\S]+?```$", markdown, re.MULTILINE)
    if matches:
        return "code"

    matches = re.findall(r"^#{1,6} ", markdown)
    if matches:
        return "heading"

    if markdown.startswith('>'):
        return "quote"

    if markdown.startswith('* ') or markdown.startswith('- '):
        return "unordered_list"

    if is_ordered_list(markdown):
        return "ordered_list"

    return "paragraph"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case 'heading':
                level = block.count('#', 0, block.index(' '))
                text = block[level + 1:].strip()

                html_blocks.append(HtmlNode(f"h{level}", children=text_to_children(text)))
            case 'paragraph':
                html_blocks.append(HtmlNode(f"p", children=text_to_children(block)))
            case 'code':
                text_node = block.strip('`')
                html_blocks.append(HtmlNode('pre', children=[HtmlNode('code', children=text_to_children(text_node))]))
            case 'quote':
                text = ""
                for line in block.split("\n"):
                    text += f"{line.lstrip('> ')}"

                html_blocks.append(HtmlNode('blockquote', children=text_to_children(text)))
            case 'unordered_list':
                items = block.split('\n')
                list_items = []
                for item in items:
                    list_items.append(HtmlNode("li", children=text_to_children(item[2:])))

                html_blocks.append(HtmlNode("ul", children=list_items))
            case 'ordered_list':
                items = block.split('\n')
                list_items = []
                for item in items:
                    list_items.append(HtmlNode("li", children=text_to_children(item[3:])))

                html_blocks.append(HtmlNode("ol", children=list_items))

    return HtmlNode("div", children=html_blocks)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    return_nodes = []
    for node in text_nodes:
        return_nodes.append(node.text_node_to_html_node())

    return return_nodes


def is_ordered_list(markdown):
    lines = markdown.strip().split("\n")

    for i, line in enumerate(lines):
        expected_number = str(i + 1)  # Should be "1", "2", "3", etc.
        match = re.match(rf"^{expected_number}\. ", line.strip())  # Strict numbering
        if not match:
            return False  # Fail if any line is incorrectly numbered

    return True
