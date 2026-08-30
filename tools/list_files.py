import os


def list_files(path: str) -> str:
    if not os.path.exists(path):
        return f"Path not found: {path}"

    items = []
    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            items.append(f"[DIR]  {item}/")
        else:
            items.append(f"[FILE] {item}")

    if not items:
        return f"Empty directory: {path}"

    return f"Contents of {path}:\n" + "\n".join(items)


if __name__ == "__main__":
    print(list_files(".."))
