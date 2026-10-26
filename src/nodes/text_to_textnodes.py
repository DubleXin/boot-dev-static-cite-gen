from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode
from src.nodes.utils.split_nodes_delimiter import split_nodes_delimiter
from src.nodes.utils.split_nodes_image import split_nodes_image
from src.nodes.utils.split_nodes_link import split_nodes_link


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "__", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
