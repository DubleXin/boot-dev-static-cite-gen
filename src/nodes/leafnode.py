from src.nodes.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ):
        super().__init__(tag, value, None, props)

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self) -> str:
        if not self.value:
            raise ValueError(f"leaf node must have value that is not {type(None)}")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
