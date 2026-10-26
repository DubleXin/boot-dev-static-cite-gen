import unittest

from src.nodes.utils.block.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_split_blocks(self):
        markdown = "# Heading\n\nFirst paragraph.\n\nSecond paragraph."

        self.assertListEqual(
            ["# Heading", "First paragraph.", "Second paragraph."],
            markdown_to_blocks(markdown),
        )

    def test_strip_and_skip_empty_blocks(self):
        markdown = "  First block.  \n\n\n\n  Second block.  \n\n   "

        self.assertListEqual(
            ["First block.", "Second block."],
            markdown_to_blocks(markdown),
        )
