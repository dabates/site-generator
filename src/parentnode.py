from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None or len(self.tag) == 0:
            raise ValueError

        if self.children is None or len(self.children) == 0:
            raise ValueError

        return_value = ''
        for child in self.children:
            return_value += child.to_html()

        return f"<{self.tag}>{self._process_children(self.children)}</{self.tag}>"

    def _process_children(self, children):
        if not children:
            return ""

        first_child = children[0].to_html()

        return first_child + self._process_children(children[1:])