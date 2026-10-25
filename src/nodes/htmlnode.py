class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.props})\n -> {self.children}"

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        return " " + "".join([f'{key}="{value}" ' for key, value in self.props.items()])
