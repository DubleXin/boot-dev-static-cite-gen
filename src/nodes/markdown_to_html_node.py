from src.nodes.htmlnode import HTMLNode
from src.nodes.leafnode import LeafNode
from src.nodes.markdown_to_textnodes import markdown_to_textnodes
from src.nodes.parentnode import ParentNode
from src.nodes.textnode.textnode import TextNode
from src.nodes.utils.block.block_to_block_type import block_to_block_type
from src.nodes.utils.block.block_type import BlockType
from src.nodes.utils.block.markdown_to_blocks import markdown_to_blocks


def get_leaf_nodes(content: str) -> list[LeafNode]:
    nodes: list[LeafNode] = []

    for text_node in markdown_to_textnodes(content):
        leaf_node = TextNode.text_node_to_html_node(text_node)

        if leaf_node is not None:
            nodes.append(leaf_node)

    return nodes


def _heading_to_html_node(block: str) -> ParentNode:
    level = len(block) - len(block.lstrip("#"))
    content = block[level + 1 :]

    return ParentNode(f"h{level}", get_leaf_nodes(content))


def _quote_to_html_node(block: str) -> ParentNode:
    content = "\n".join(line[1:].lstrip() for line in block.split("\n"))

    return ParentNode("blockquote", get_leaf_nodes(content))


def _create_list_items(contents: list[str]) -> list[ParentNode]:
    return [ParentNode("li", get_leaf_nodes(content)) for content in contents]


def _unordered_list_to_html_node(block: str) -> ParentNode:
    contents = [line[2:] for line in block.split("\n")]

    return ParentNode("ul", _create_list_items(contents))


def _ordered_list_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    first_number = int(lines[0][: lines[0].index(".")])
    start_from = max(1, first_number)

    contents = [line[line.index(".") + 2 :] for line in lines]
    items = _create_list_items(contents)

    return ParentNode("ol", items, {"start": start_from})


def _block_to_html_node(block: str) -> ParentNode | None:
    match block_to_block_type(block):
        case BlockType.PARAGRAPH:
            return ParentNode("p", get_leaf_nodes(block))

        case BlockType.CODE:
            return ParentNode("pre", [LeafNode("code", block[4:-3])])

        case BlockType.HEADING:
            return _heading_to_html_node(block)

        case BlockType.QUOTE:
            return _quote_to_html_node(block)

        case BlockType.ULIST:
            return _unordered_list_to_html_node(block)

        case BlockType.OLIST:
            return _ordered_list_to_html_node(block)

    return None


def markdown_to_html_node(markdown_document: str) -> ParentNode:
    children: list[HTMLNode] = []

    for block in markdown_to_blocks(markdown_document):
        node = _block_to_html_node(block)

        if node is not None:
            children.append(node)

    return ParentNode("main", children)
