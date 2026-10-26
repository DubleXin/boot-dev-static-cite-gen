from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    if not old_nodes:
        return old_nodes

    nodes: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        parts = old_node.text.split(delimiter)

        if len(parts) % 2 == 0:
            nodes.append(old_node)
            continue

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                nodes.append(TextNode(part, TextType.TEXT))
            else:
                nodes.append(TextNode(part, text_type))

    return nodes
