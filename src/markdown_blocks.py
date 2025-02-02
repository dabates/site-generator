import re

from src.textnode import TextType


def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.strip().split('\n\n'):
        blocks.append(block.strip())

    return blocks


def block_to_block_type(markdown):
    matches = re.findall(r"^```[\s\S]+?```$", markdown, re.MULTILINE)
    if matches:
        return "code"

    matches = re.findall(r"^#{1,6} ", markdown)
    if matches:
        return "heading"

    if markdown.startswith('>'):
        return "quote"

    if markdown.startswith('* ') or markdown.startswith('- '):
        return "unordered_list"

    if is_ordered_list(markdown):
        return "ordered_list"

    return "paragraph"


def is_ordered_list(markdown):
    lines = markdown.strip().split("\n")

    for i, line in enumerate(lines):
        expected_number = str(i + 1)  # Should be "1", "2", "3", etc.
        match = re.match(rf"^{expected_number}\. ", line.strip())  # Strict numbering
        if not match:
            return False  # Fail if any line is incorrectly numbered

    return True
