import unittest

from src.view_builder.utils.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_heading_at_document_start(self):
        markdown = "# Title\n\nParagraph."

        self.assertEqual("Title", extract_title(markdown))

    def test_heading_after_paragraph(self):
        markdown = "Introductory paragraph.\n\n# Title\n\nAnother paragraph."

        self.assertEqual("Title", extract_title(markdown))

    def test_heading_without_trailing_newline(self):
        self.assertEqual("Title", extract_title("# Title"))

    def test_heading_with_trailing_newline(self):
        self.assertEqual("Title", extract_title("# Title\n"))

    def test_heading_followed_by_single_newline(self):
        markdown = "# Title\nParagraph immediately after the heading."

        self.assertEqual("Title", extract_title(markdown))

    def test_heading_at_document_end(self):
        markdown = "Introductory paragraph.\n\n# Title"

        self.assertEqual("Title", extract_title(markdown))

    def test_heading_whitespace_is_stripped(self):
        markdown = "#   Title with spaces   \n\nParagraph."

        self.assertEqual("Title with spaces", extract_title(markdown))

    def test_heading_preserves_internal_spaces(self):
        markdown = "# Title  with  spaces"

        self.assertEqual("Title  with  spaces", extract_title(markdown))

    def test_first_h1_is_returned(self):
        markdown = "# First title\n\nParagraph.\n\n# Second title"

        self.assertEqual("First title", extract_title(markdown))

    def test_other_heading_before_h1(self):
        markdown = "## Subtitle\n\n# Main title\n\nParagraph."

        self.assertEqual("Main title", extract_title(markdown))

    def test_missing_h1(self):
        documents = [
            "",
            "   ",
            "An ordinary paragraph.",
            "First paragraph.\n\nSecond paragraph.",
            "#Title without a space",
            "This contains # a hash.",
        ]

        for markdown in documents:
            with self.subTest(markdown=markdown):
                self.assertRaises(ValueError, extract_title, markdown)

    def test_other_heading_levels_are_not_h1(self):
        for level in range(2, 7):
            with self.subTest(level=level):
                markdown = f"{'#' * level} Heading"

                with self.assertRaises(ValueError):
                    extract_title(markdown)
