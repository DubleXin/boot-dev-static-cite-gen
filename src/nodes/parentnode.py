from src.nodes.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError(
                f"The tag member of parent node must be different from {type(None)}"
            )
        if not self.children:
            raise ValueError(
                f"The children member of parent node must exist; actual value is type of: {type(None)}"
            )

        children_html: list[str] = []
        for child in self.children:
            children_html.append(child.to_html())

        return (
            f"<{self.tag}{self.props_to_html()}>{''.join(children_html)}</{self.tag}>"
        )
