def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return f"File contents of {path}:\n{content}"


if __name__ == "__main__":
    print(read_file("../main.py"))
