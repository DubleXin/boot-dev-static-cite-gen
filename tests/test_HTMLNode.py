import unittest

from src.nodes.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "link to", None, {"href": "#footer", "color": "red"})
        self.assertEqual(
            f"{node}",
            f"HTMLNode(a, link to, { ({'href': '#footer', 'color': 'red'}) })\n -> {None}",
        )

    def test_to_html(self):
        node = HTMLNode("a", "link to", None, {"href": "#footer", "color": "red"})
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode("a", "link to", None, {"href": "#footer", "color": "red"})
        self.assertEqual(node.props_to_html(), ' href="#footer" color="red" ')
