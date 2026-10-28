import unittest

from src.nodes.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        node = markdown_to_html_node("This is a paragraph.")

        self.assertEqual(
            "<main><p>This is a paragraph.</p></main>",
            node.to_html(),
        )

    def test_heading_levels(self):
        for level in range(1, 7):
            with self.subTest(level=level):
                markdown = f"{'#' * level} Heading"
                node = markdown_to_html_node(markdown)

                self.assertEqual(
                    f"<main><h{level}>Heading</h{level}></main>",
                    node.to_html(),
                )

    def test_inline_formatting(self):
        node = markdown_to_html_node("Text with **bold**, _italic_ and `code`.")

        self.assertEqual(
            "<main><p>"
            "Text with <b>bold</b>, <i>italic</i> and <code>code</code>."
            "</p></main>",
            node.to_html(),
        )

    def test_code_preserves_literal_markup(self):
        node = markdown_to_html_node("```\n**bold** and _italic_\n```")

        self.assertEqual(
            "<main><pre><code>**bold** and _italic_\n</code></pre></main>",
            node.to_html(),
        )

    def test_quote(self):
        node = markdown_to_html_node("> First line\n> Second line")

        self.assertEqual(
            "<main><blockquote>First line\nSecond line</blockquote></main>",
            node.to_html(),
        )

    def test_unordered_list(self):
        node = markdown_to_html_node("- First item\n- Second item\n- Third item")

        self.assertEqual(
            "<main><ul>"
            "<li>First item</li>"
            "<li>Second item</li>"
            "<li>Third item</li>"
            "</ul></main>",
            node.to_html(),
        )

    def test_ordered_list_starting_from_one(self):
        node = markdown_to_html_node("1. First item\n2. Second item")
        ordered_list = node.children[0]

        self.assertEqual("ol", ordered_list.tag)
        self.assertEqual({"start": 1}, ordered_list.props)
        self.assertListEqual(
            ["<li>First item</li>", "<li>Second item</li>"],
            [item.to_html() for item in ordered_list.children],
        )

    def test_ordered_list_keeps_more_than_four_items(self):
        node = markdown_to_html_node(
            "3. First item\n"
            "4. Second item\n"
            "5. Third item\n"
            "6. Fourth item\n"
            "7. Fifth item\n"
            "8. Sixth item"
        )
        ordered_list = node.children[0]

        self.assertEqual("ol", ordered_list.tag)
        self.assertEqual({"start": 3}, ordered_list.props)
        self.assertEqual(6, len(ordered_list.children))
        self.assertListEqual(
            [
                "<li>First item</li>",
                "<li>Second item</li>",
                "<li>Third item</li>",
                "<li>Fourth item</li>",
                "<li>Fifth item</li>",
                "<li>Sixth item</li>",
            ],
            [item.to_html() for item in ordered_list.children],
        )

    def test_inline_formatting_inside_list_items(self):
        node = markdown_to_html_node("- **Bold item**\n- Item with `code`")

        self.assertEqual(
            "<main><ul>"
            "<li><b>Bold item</b></li>"
            "<li>Item with <code>code</code></li>"
            "</ul></main>",
            node.to_html(),
        )

    def test_image(self):
        node = markdown_to_html_node("![An image](https://example.com/image.png)")
        paragraph = node.children[0]
        image = paragraph.children[0]

        self.assertEqual("p", paragraph.tag)
        self.assertEqual(1, len(paragraph.children))
        self.assertEqual("img", image.tag)
        self.assertEqual(
            {
                "src": "https://example.com/image.png",
                "alt": "An image",
            },
            image.props,
        )

    def test_link(self):
        node = markdown_to_html_node("[Example](https://example.com)")
        paragraph = node.children[0]
        link = paragraph.children[0]

        self.assertEqual("p", paragraph.tag)
        self.assertEqual(1, len(paragraph.children))
        self.assertEqual("a", link.tag)
        self.assertEqual("Example", link.value)
        self.assertEqual(
            {"href": "https://example.com"},
            link.props,
        )

    def test_multiple_blocks_preserve_order(self):
        markdown = (
            "# Heading\n\n"
            "A paragraph.\n\n"
            "- First item\n"
            "- Second item\n\n"
            "Another paragraph."
        )
        node = markdown_to_html_node(markdown)

        self.assertEqual("main", node.tag)
        self.assertEqual(
            "<main>"
            "<h1>Heading</h1>"
            "<p>A paragraph.</p>"
            "<ul><li>First item</li><li>Second item</li></ul>"
            "<p>Another paragraph.</p>"
            "</main>",
            node.to_html(),
        )
