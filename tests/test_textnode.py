import unittest

from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_arguments(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode(
            "This is a text node", TextType.ITALIC, url="./tests/test_textnode.py"
        )
        self.assertNotEqual(node, node2)

    def test_different_type_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = {"This is a text node", TextType.BOLD}
        self.assertNotEqual(node, node2)

    def test_text(self):
        text_node = TextNode("this is a text node", TextType.TEXT)
        html_text_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_text_node.tag, None)
        self.assertEqual(html_text_node.value, "this is a text node")
        non_exist_node = TextNode("not a valid node", "invalid")
        html_non_exist_node = TextNode.text_node_to_html_node(non_exist_node)
        self.assertEqual(html_non_exist_node, None)
        tag_node = TextNode("bold text", TextType.BOLD)
        html_tag_node = TextNode.text_node_to_html_node(tag_node)
        self.assertEqual(html_tag_node.tag, "b")
        self.assertEqual(html_tag_node.value, "bold text")
        ancor_node = TextNode("link", TextType.LINK, "#footer")
        html_ancor_node = TextNode.text_node_to_html_node(ancor_node)
        self.assertEqual(html_ancor_node.tag, "a")
        self.assertEqual(html_ancor_node.value, "link")
        self.assertEqual(html_ancor_node.props, {"href": "#footer"})
        img_node = TextNode(
            "my bank credentials",
            TextType.IMAGE,
            "https://static.wikia.nocookie.net/dqw4w9wgxcq/images/0/08/Site-background-dark/revision/latest?cb=20220428173233",
        )
        html_img_node = TextNode.text_node_to_html_node(img_node)
        self.assertEqual(html_img_node.tag, "img")
        self.assertEqual(html_img_node.value, "")
        self.assertEqual(
            html_img_node.props,
            {
                "src": "https://static.wikia.nocookie.net/dqw4w9wgxcq/images/0/08/Site-background-dark/revision/latest?cb=20220428173233",
                "alt": img_node.text,
            },
        )


if __name__ == "__main__":
    unittest.main()
