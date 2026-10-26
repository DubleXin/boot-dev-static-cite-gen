from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode
from src.nodes.utils.extract_images import extract_markdown_images


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        return old_nodes

    nodes: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        all_images = extract_markdown_images(old_node.text)

        if not all_images:
            nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for alt, link in all_images:
            before, remaining_text = remaining_text.split(f"![{alt}]({link})", 1)

            if before:
                nodes.append(TextNode(before, TextType.TEXT))

            nodes.append(TextNode(alt, TextType.IMAGE, link))

        if remaining_text:
            nodes.append(TextNode(remaining_text, TextType.TEXT))

    return nodes
