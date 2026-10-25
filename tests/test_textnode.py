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


if __name__ == "__main__":
    unittest.main()
