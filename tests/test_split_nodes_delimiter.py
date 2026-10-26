import unittest

from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode
from src.nodes.utils.inline.split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delimiters(self):
        node_single = TextNode("lorem _ipsum_ dolor", TextType.TEXT)
        node_list_single = [node_single]
        new_node_list_single = split_nodes_delimiter(
            node_list_single, "_", TextType.ITALIC
        )
        self.assertNotEqual(node_list_single, new_node_list_single)
        self.assertEqual(len(new_node_list_single), 3)
        self.assertEqual(new_node_list_single[0], TextNode("lorem ", TextType.TEXT))
        self.assertEqual(new_node_list_single[1], TextNode("ipsum", TextType.ITALIC))

        node_double = TextNode("lorem __ipsum__ dolor", TextType.TEXT)
        node_list_double = [node_double]
        new_node_list_double = split_nodes_delimiter(
            node_list_single, "_", TextType.BOLD
        )
        self.assertNotEqual(node_list_double, new_node_list_double)
        self.assertEqual(len(new_node_list_double), 3)
        self.assertEqual(new_node_list_double[0], TextNode("lorem ", TextType.TEXT))
        self.assertEqual(new_node_list_double[1], TextNode("ipsum", TextType.BOLD))

    def test_only_decorated(self):
        node = TextNode("**lorem ipsum dolor**", TextType.TEXT)
        node_list = [node]
        new_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)

        self.assertEqual(len(new_list), 1)
        self.assertEqual(new_list[0], TextNode("lorem ipsum dolor", TextType.BOLD))
        node = TextNode("*x*", TextType.TEXT)

        node_list = [node]
        new_list = split_nodes_delimiter(node_list, "*", TextType.ITALIC)
        self.assertEqual(new_list[0], TextNode("x", TextType.ITALIC))

        node = TextNode("**x**", TextType.TEXT)

        node_list = [node]
        new_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
        self.assertEqual(new_list[0], TextNode("x", TextType.BOLD))

    def test_plain(self):
        node = TextNode("lorem ipsum dolor", TextType.TEXT)
        node_list = [node]
        new_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)

        self.assertEqual(len(new_list), 1)
        self.assertEqual(new_list[0], TextNode("lorem ipsum dolor", TextType.TEXT))

    def test_multiple_delimiter_sets(self):
        node = TextNode("Lorem _ipsum_ dolor _sit_ amet", TextType.TEXT)
        node_list = [node]
        new_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)

        self.assertEqual(len(new_list), 5)
        self.assertEqual(
            new_list,
            [
                TextNode("Lorem ", TextType.TEXT),
                TextNode("ipsum", TextType.ITALIC),
                TextNode(" dolor ", TextType.TEXT),
                TextNode("sit", TextType.ITALIC),
                TextNode(" amet", TextType.TEXT),
            ],
        )

    def test_multiple_parses(self):
        node = TextNode("Lorem _ipsum_ *dolor* __sit__ amet", TextType.TEXT)
        node_list = [node]
        node_list = split_nodes_delimiter(node_list, "__", TextType.BOLD)
        node_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
        node_list = split_nodes_delimiter(node_list, "*", TextType.ITALIC)
        self.assertEqual(
            node_list,
            [
                TextNode("Lorem ", TextType.TEXT),
                TextNode("ipsum", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("dolor", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("sit", TextType.BOLD),
                TextNode(" amet", TextType.TEXT),
            ],
        )

    def test_empty(self):
        node = TextNode("", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(node_list, [])
        node = TextNode("_", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "_", TextType.BOLD)
        self.assertEqual(node_list, [node])
        node = TextNode("__", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "_", TextType.BOLD)
        self.assertEqual(node_list, [])
        node = TextNode("__", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(node_list, [node])
        node = TextNode("_", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(node_list, [node])

    def test_not_closed(self):
        node = TextNode("__a_", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(node_list, [node])
        node = TextNode("__a", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertEqual(node_list, [node])
        node = TextNode("_a", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "_", TextType.BOLD)
        self.assertEqual(node_list, [node])
