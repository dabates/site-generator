from enum import Enum

from src.leafnode import LeafNode


class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text, None)
            case TextType.BOLD:
                return LeafNode('b', self.text, None)
            case TextType.ITALIC:
                return LeafNode('i', self.text, None)
            case TextType.CODE:
                return LeafNode('code', self.text, None)
            case TextType.LINK:
                return LeafNode('a', self.text, {"href": self.url})
            case TextType.IMAGE:
                return LeafNode('img', '', {"src": self.url, "alt": self.text})

        raise Exception(f"Invalid text type: {self.text_type}")
