import os
import shutil


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


# Run the script
if __name__ == "__main__":
    sync_directories()
