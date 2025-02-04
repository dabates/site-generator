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
        attribs = [
            f'text="{self.text}"' if self.text is not None else None,
            f'text_type="{self.text_type.value}"' if self.text_type is not None else None,
            f'url="{self.url}"' if self.url is not None else None,
        ]

        return_str = ", ".join(filter(None, attribs))

        return f"TextNode({return_str})"

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
