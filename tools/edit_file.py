import os


def edit_file(path: str, old_text: str, new_text: str) -> str:
    if os.path.exists(path) and old_text:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        if old_text not in content:
            return f"Text not found in file: {old_text}"

        content = content.replace(old_text, new_text)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Successfully edited {path}"
    else:
        # Only create directory if path contains subdirectories
        dir_name = os.path.dirname(path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)

        return f"Successfully created {path}"


if __name__ == "__main__":
    edit_file(
        path="test.txt",
        old_text="Hello world!",
        new_text="Hello world! How are you?",
    )
