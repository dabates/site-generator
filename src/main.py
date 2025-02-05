import os
import shutil

from src.markdown_blocks import extract_title, markdown_to_html_node


def copy_recursive(src, dest):
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
        return

    # Ensure destination directory exists
    os.makedirs(dest, exist_ok=True)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):
            print(f"Creating directory: {dest_path}")
            copy_recursive(src_path, dest_path)
        elif os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dest_path}")
            shutil.copy2(src_path, dest_path)  # Use copy2 to preserve metadata


def sync_directories():
    src = "static"
    dest = "public"

    if os.path.exists(dest):
        print(f"Deleting existing contents of '{dest}'")
        shutil.rmtree(dest)

    print(f"Copying contents from '{src}' to '{dest}'")
    copy_recursive(src, dest)

    print("Sync complete!")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as from_file:
        markdown = from_file.read()

    with open(template_path) as template_file:
        template_content = template_file.read()

    page_title = extract_title(markdown)

    html_content = template_content.replace("{{ Title }}", page_title)
    html_content = html_content.replace("{{ Content }}", markdown_to_html_node(markdown).to_html())

    with open(dest_path, "w") as out_file:
        out_file.write(html_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        print(f"Source '{dest_dir_path}' does not exist.")
        return

    # Ensure destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)

    for item in os.listdir(dir_path_content):
        extension = item.split(".")[-1]

        src_path = os.path.join(dir_path_content, item)
        if os.path.isdir(src_path):
            dest_path = os.path.join(dest_dir_path, item)
        else:
            dest_path = os.path.join(dest_dir_path, item.replace(f".{extension}", ".html"))

        if os.path.isdir(src_path):
            print(f"Creating directory: {dest_path}")
            generate_pages_recursive(src_path, template_path, dest_path)
        elif os.path.isfile(src_path):
            print(f"Generating file: {src_path} -> {dest_path}")
            generate_page(src_path, template_path, dest_path)


# Run the script
if __name__ == "__main__":
    sync_directories()
    generate_pages_recursive('content', 'template.html', 'public')
