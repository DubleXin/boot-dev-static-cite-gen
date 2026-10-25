import unittest

from src.nodes.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_children(self):
        node = LeafNode("p", "lorem ipsum.", {"color": "green"})
        self.assertEqual(node.children, None)

    def test_to_html(self):
        node = LeafNode("a", "link to", {"href": "#footer", "color": "red"})
        self.assertEqual(node.to_html(), '<a href="#footer" color="red" >link to</a>')

    def test_repr(self):
        node = LeafNode("p", "lorem ipsum.", {"color": "green"})
        self.assertEqual(
            f"{node}",
            f"LeafNode(p, lorem ipsum., { ({'color': 'green'}) })",
        )
