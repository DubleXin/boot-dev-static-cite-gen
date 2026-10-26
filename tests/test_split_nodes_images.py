import unittest

from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode
from src.nodes.utils.split_nodes_image import split_nodes_image


class TestSplitNodesImages(unittest.TestCase):
    def test_multiple_images_with_text(self):
        node = TextNode(
            "This is text with an "
            "![image](https://i.imgur.com/zjjcJKZ.png)"
            " and another "
            "![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            split_nodes_image([node]),
        )

    def test_image_at_end(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
            ],
            split_nodes_image([node]),
        )

    def test_image_at_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(" and another", TextType.TEXT),
            ],
            split_nodes_image([node]),
        )

    def test_adjacent_images(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)"
            "![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            split_nodes_image([node]),
        )

    def test_text_without_images(self):
        node = TextNode("This is text", TextType.TEXT)

        self.assertListEqual(
            [TextNode("This is text", TextType.TEXT)],
            split_nodes_image([node]),
        )

    def test_only_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
            ],
            split_nodes_image([node]),
        )
