import unittest

from src.nodes.text_to_textnodes import text_to_textnodes
from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode


class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        self.assertListEqual(
            [TextNode("This is plain text.", TextType.TEXT)],
            text_to_textnodes("This is plain text."),
        )

    def test_bold_asterisks(self):
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
            text_to_textnodes("Some **bold** text."),
        )

    def test_bold_underscores(self):
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
            text_to_textnodes("Some __bold__ text."),
        )

    def test_italic_asterisks(self):
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
            text_to_textnodes("Some *italic* text."),
        )

    def test_italic_underscores(self):
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
            text_to_textnodes("Some _italic_ text."),
        )

    def test_code(self):
        self.assertListEqual(
            [
                TextNode("Run ", TextType.TEXT),
                TextNode("print(1)", TextType.CODE),
                TextNode(" now.", TextType.TEXT),
            ],
            text_to_textnodes("Run `print(1)` now."),
        )

    def test_image(self):
        self.assertListEqual(
            [
                TextNode("An ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://example.com/image.png",
                ),
                TextNode(" here.", TextType.TEXT),
            ],
            text_to_textnodes("An ![image](https://example.com/image.png) here."),
        )

    def test_link(self):
        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("site", TextType.LINK, "https://example.com"),
                TextNode(" today.", TextType.TEXT),
            ],
            text_to_textnodes("Visit [site](https://example.com) today."),
        )

    def test_mixed_markup(self):
        text = (
            "This is **bold** with _italic_ and `code`, "
            "an ![image](https://example.com/image.png) "
            "and a [link](https://example.com)."
        )

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(", an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://example.com/image.png",
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(".", TextType.TEXT),
            ],
            text_to_textnodes(text),
        )

    def test_only_formatted_text(self):
        self.assertListEqual(
            [TextNode("bold", TextType.BOLD)],
            text_to_textnodes("**bold**"),
        )

    def test_adjacent_formats(self):
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code", TextType.CODE),
            ],
            text_to_textnodes("**bold**_italic_`code`"),
        )

    def test_repeated_format(self):
        self.assertListEqual(
            [
                TextNode("first", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("second", TextType.BOLD),
            ],
            text_to_textnodes("**first** and **second**"),
        )

    def test_both_bold_delimiters(self):
        self.assertListEqual(
            [
                TextNode("first", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("second", TextType.BOLD),
            ],
            text_to_textnodes("__first__ and **second**"),
        )

    def test_both_italic_delimiters(self):
        self.assertListEqual(
            [
                TextNode("first", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("second", TextType.ITALIC),
            ],
            text_to_textnodes("_first_ and *second*"),
        )
