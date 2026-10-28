from src.nodes.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] | None = None,
        has_closing_tag: bool = True,
    ):
        super().__init__(tag, value, None, props)
        self.has_closing_tag = has_closing_tag

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self) -> str:
        if not self.value:
            raise ValueError(
                f"The value member of leaf node must be different from {type(None)}"
            )
        if not self.tag:
            return self.value
        if self.has_closing_tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>"
