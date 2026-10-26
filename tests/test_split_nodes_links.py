import unittest

from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode
from src.nodes.utils.split_nodes_link import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):
    def test_multiple_links_with_text(self):
        node = TextNode(
            "Visit [first](https://example.com/1)"
            " and [second](https://example.com/2) today.",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("first", TextType.LINK, "https://example.com/1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("second", TextType.LINK, "https://example.com/2"),
                TextNode(" today.", TextType.TEXT),
            ],
            split_nodes_link([node]),
        )

    def test_link_at_end(self):
        node = TextNode(
            "Visit [first](https://example.com/1)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("first", TextType.LINK, "https://example.com/1"),
            ],
            split_nodes_link([node]),
        )

    def test_link_at_start(self):
        node = TextNode(
            "[first](https://example.com/1) is useful.",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("first", TextType.LINK, "https://example.com/1"),
                TextNode(" is useful.", TextType.TEXT),
            ],
            split_nodes_link([node]),
        )

    def test_adjacent_links(self):
        node = TextNode(
            "[first](https://example.com/1)[second](https://example.com/2)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("first", TextType.LINK, "https://example.com/1"),
                TextNode("second", TextType.LINK, "https://example.com/2"),
            ],
            split_nodes_link([node]),
        )

    def test_only_link(self):
        node = TextNode(
            "[first](https://example.com/1)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("first", TextType.LINK, "https://example.com/1"),
            ],
            split_nodes_link([node]),
        )

    def test_repeated_identical_links(self):
        node = TextNode(
            "[same](https://example.com) and [same](https://example.com)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("same", TextType.LINK, "https://example.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("same", TextType.LINK, "https://example.com"),
            ],
            split_nodes_link([node]),
        )

    def test_text_without_links(self):
        node = TextNode("This is plain text.", TextType.TEXT)

        self.assertListEqual([node], split_nodes_link([node]))

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)

        self.assertListEqual([node], split_nodes_link([node]))

    def test_empty_nodes(self):
        self.assertListEqual([], split_nodes_link([]))

    def test_non_text_node_is_preserved(self):
        node = TextNode(
            "[first](https://example.com/1)",
            TextType.IMAGE,
            "https://example.com/image.png",
        )

        self.assertListEqual([node], split_nodes_link([node]))

    def test_multiple_input_nodes(self):
        old_nodes = [
            TextNode("Plain text.", TextType.TEXT),
            TextNode("[first](https://example.com/1)", TextType.TEXT),
            TextNode("More text.", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("Plain text.", TextType.TEXT),
                TextNode("first", TextType.LINK, "https://example.com/1"),
                TextNode("More text.", TextType.TEXT),
            ],
            split_nodes_link(old_nodes),
        )

    def test_image_is_not_treated_as_link(self):
        node = TextNode(
            "![image](https://example.com/image.png)",
            TextType.TEXT,
        )

        self.assertListEqual([node], split_nodes_link([node]))
