from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode
from src.nodes.utils.extract_links import extract_markdown_links


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        return old_nodes

    nodes: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        all_links = extract_markdown_links(old_node.text)

        if not all_links:
            nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for text, link in all_links:
            before, remaining_text = remaining_text.split(f"[{text}]({link})", 1)

            if before:
                nodes.append(TextNode(before, TextType.TEXT))

            nodes.append(TextNode(text, TextType.LINK, link))

        if remaining_text:
            nodes.append(TextNode(remaining_text, TextType.TEXT))

    return nodes
