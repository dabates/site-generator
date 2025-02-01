import re

from src.textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception(f"Unmatched delimiter: {delimiter} in text: {node.text}")

        for i, segment in enumerate(split_text):
            if segment:
                new_nodes.append(TextNode(segment, text_type if i % 2 else TextType.NORMAL))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)
            continue

        for alt, url in images:
            split_text = text.split(f"![{alt}]({url})", 1)
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], TextType.NORMAL))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            text = split_text[1] if len(split_text) > 1 else ""

        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        for alt, url in links:
            split_text = text.split(f"[{alt}]({url})", 1)
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], TextType.NORMAL))

            new_nodes.append(TextNode(alt, TextType.LINK, url))

            text = split_text[1] if len(split_text) > 1 else ""

        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
