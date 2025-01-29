from enum import Enum


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
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children
