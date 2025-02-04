class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""

        return " " + " ".join(map(lambda d: f'{d[0]}="{d[1]}"', self.props.items()))

    def __repr__(self):
        attribs = [
            f'tag="{self.tag}"' if self.tag is not None else None,
            f'value="{self.value}"' if self.value is not None else None,
            f'children="{self.children}"' if self.children is not None else None,
            f'props="{self.props}"' if self.props is not None else None,
        ]

        return_str = ", ".join(filter(None, attribs))

        return f"HtmlNode({return_str})"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children
