from src.htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None or self.value == '':
            raise ValueError

        if self.tag is None:
            return self.value

        return super().to_html()
