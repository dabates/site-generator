import unittest

from src.text_utils import extract_markdown_images, extract_markdown_links


class ExtractMarkdownImages(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        images = extract_markdown_images(text)

        self.assertEqual(images, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
        ])

    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        link = extract_markdown_links(text)

        self.assertEqual(link, [
            ("to boot dev", "https://www.boot.dev"),
        ])

    def test_extract_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)

        self.assertEqual(images, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_extract_multiple_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        link = extract_markdown_links(text)

        self.assertEqual(link, [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])


if __name__ == '__main__':
    unittest.main()
