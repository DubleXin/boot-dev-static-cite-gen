import unittest

from src.nodes.leafnode import LeafNode
from src.nodes.parentnode import ParentNode


class TestParenNode(unittest.TestCase):
    def test_children_member(self):
        node = ParentNode(
            "div",
            [
                LeafNode("a", "link 1", {"href": "#header"}),
                LeafNode("a", "link 2", {"href": "#content"}),
                LeafNode("a", "link 3", {"href": "#footer"}),
            ],
            {"background": "teal"},
        )
        self.assertEqual(
            node.children,
            [
                LeafNode("a", "link 1", {"href": "#header"}),
                LeafNode("a", "link 2", {"href": "#content"}),
                LeafNode("a", "link 3", {"href": "#footer"}),
            ],
        )

    def test_to_html(self):
        node_link_list = ParentNode(
            "div",
            [
                LeafNode("a", "link 1", {"href": "#header"}),
                LeafNode("a", "link 2", {"href": "#content"}),
                LeafNode("a", "link 3", {"href": "#footer"}),
            ],
            {"background": "teal"},
        )
        self.assertEqual(
            node_link_list.to_html(),
            '<div background="teal" ><a href="#header" >link 1</a><a href="#content" >link 2</a><a href="#footer" >link 3</a></div>',
        )

        node_nested_div = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("a", "link 1", {"href": "#header"}),
                        LeafNode("a", "link 2", {"href": "#content"}),
                        LeafNode("a", "link 3", {"href": "#footer"}),
                    ],
                    {"background": "red"},
                )
            ],
            {"background": "teal"},
        )

        self.assertEqual(
            node_nested_div.to_html(),
            '<div background="teal" ><div background="red" ><a href="#header" >link 1</a><a href="#content" >link 2</a><a href="#footer" >link 3</a></div></div>',
        )

        node_multiple_nested_elemnts = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("a", "link 1", {"href": "#header"}),
                        LeafNode("a", "link 2", {"href": "#content"}),
                        LeafNode("a", "link 3", {"href": "#footer"}),
                    ],
                    {"background": "red"},
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "lorem"),
                        LeafNode("span", "not ipsum", {"color": "blue"}),
                        LeafNode(None, "ipsum"),
                    ],
                    {"text-align": "center"},
                ),
                ParentNode("div", [ParentNode("div", [LeafNode("p", "usless text")])]),
            ],
            {"background": "teal"},
        )
        self.assertEqual(
            node_multiple_nested_elemnts.to_html(),
            '<div background="teal" ><div background="red" ><a href="#header" >link 1</a><a href="#content" >link 2</a><a href="#footer" >link 3</a></div><p text-align="center" >lorem<span color="blue" >not ipsum</span>ipsum</p><div><div><p>usless text</p></div></div></div>',
        )

    def test_missing_members(self):
        node = ParentNode(
            "div",
            None,
            {"background": "teal"},
        )
        self.assertRaises(ValueError, node.to_html)
        node = ParentNode(
            None,
            [
                LeafNode("a", "link 1", {"href": "#header"}),
                LeafNode("a", "link 2", {"href": "#content"}),
                LeafNode("a", "link 3", {"href": "#footer"}),
            ],
            {"background": "teal"},
        )
        self.assertRaises(ValueError, node.to_html)
