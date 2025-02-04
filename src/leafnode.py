from src.htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        attribs = [
            f'tag="{self.tag}"' if self.tag is not None else None,
            f'value="{self.value}"' if self.value is not None else None,
            f'children="{self.children}"' if self.children is not None else None,
            f'props="{self.props}"' if self.props is not None else None,
        ]

        return_str = ", ".join(filter(None, attribs))

        return f"LeafNode({return_str})"

    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
