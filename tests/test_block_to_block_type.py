import unittest

from src.nodes.utils.block.block_to_block_type import block_to_block_type
from src.nodes.utils.block.block_type import BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is an ordinary paragraph."

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_multiline_paragraph(self):
        block = "First line.\nSecond line."

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_empty_block(self):
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(""))

    def test_heading_levels(self):
        for level in range(1, 7):
            with self.subTest(level=level):
                block = f"{'#' * level} Heading"

                self.assertEqual(
                    BlockType.HEADING,
                    block_to_block_type(block),
                )

    def test_heading_without_space(self):
        block = "##Heading"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_heading_with_too_many_hashes(self):
        block = "####### Heading"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_hash_inside_paragraph(self):
        block = "This contains # a hash."

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_code(self):
        block = "```\nprint('Hello')\n```"

        self.assertEqual(BlockType.CODE, block_to_block_type(block))

    def test_code_containing_other_markup(self):
        block = "```\n# Heading\n> Quote\n- Item\n1. Item\n```"

        self.assertEqual(BlockType.CODE, block_to_block_type(block))

    def test_code_without_closing_fence(self):
        block = "```\nprint('Hello')"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_code_without_opening_newline(self):
        block = "```print('Hello')```"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_quote(self):
        block = (
            "> The deeds of Glorfindel shine bright.\n"
            "> Whilst the feats of others flicker."
        )

        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_quote_without_space(self):
        block = ">First line\n>Second line"

        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_quote_with_unmarked_line(self):
        block = "> First line\nSecond line"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_unordered_list(self):
        block = "- First item\n- Second item\n- Third item"

        self.assertEqual(BlockType.ULIST, block_to_block_type(block))

    def test_unordered_list_without_space(self):
        block = "-First item\n-Second item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_unordered_list_with_unmarked_line(self):
        block = "- First item\nSecond item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"

        self.assertEqual(BlockType.OLIST, block_to_block_type(block))

    def test_ordered_list_with_double_digit_numbers(self):
        block = "\n".join(f"{number}. Item {number}" for number in range(1, 12))

        self.assertEqual(BlockType.OLIST, block_to_block_type(block))

    def test_ordered_list_starting_from_two(self):
        block = "2. First item\n3. Second item"

        self.assertEqual(BlockType.OLIST, block_to_block_type(block))

    def test_ordered_list_with_skipped_number(self):
        block = "1. First item\n3. Third item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_ordered_list_with_repeated_number(self):
        block = "1. First item\n1. Second item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_ordered_list_without_space(self):
        block = "1.First item\n2.Second item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_ordered_list_with_unmarked_line(self):
        block = "1. First item\nSecond item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_empty_line_breaks_quote_or_list(self):
        blocks = [
            "> First line\n\n> Second line",
            "- First item\n\n- Second item",
            "1. First item\n\n2. Second item",
        ]

        for block in blocks:
            with self.subTest(block=block):
                self.assertEqual(
                    BlockType.PARAGRAPH,
                    block_to_block_type(block),
                )
