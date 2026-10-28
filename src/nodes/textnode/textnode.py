from collections.abc import Callable

from src.nodes.leafnode import LeafNode
from src.nodes.textnode.text_type import TextType


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        return (
            type(self) == type(other)
            and self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    @staticmethod
    def text_node_to_html_node(text_node: "TextNode") -> LeafNode | None:
        get_node: Callable[[str | None], LeafNode] = lambda tag: LeafNode(
            tag, text_node.text
        )
        return {
            TextType.TEXT: get_node(None),
            TextType.BOLD: get_node("b"),
            TextType.ITALIC: get_node("i"),
            TextType.CODE: get_node("code"),
            TextType.LINK: LeafNode("a", text_node.text, {"href": text_node.url}),
            TextType.IMAGE: LeafNode(
                "img",
                " ",
                {"src": text_node.url, "alt": text_node.text},
                has_closing_tag=False,
            ),
        }.get(text_node.text_type, None)
