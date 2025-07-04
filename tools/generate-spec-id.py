import hashlib
import re

def generate_spec_id(title: str, author: str, version: str, length: int = 8) -> str:
    input_str = f"{author}|{title}|{version}"
    print("\nid: spec:"+ input_str)
    hash_digest = hashlib.sha256(input_str.encode()).hexdigest()
    return f"spec:{hash_digest[:length]}"


def main():
    print("Corgi Spec ID Generator")
    author = input("Author (e.g. @yourname): ").strip()
    if not author.startswith('@'):
        author = '@'  + author
    VALID_HANDLE = re.compile(r"^@([a-z0-9.-]+)$")
    if VALID_HANDLE.match(author) is None:
        print("❗ Author handles must use only lowercase letters, numbers, dashes (`-`), and dots (`.`)")
        return

    title = input("Title: ").strip()
    version = input("Version (default 0.1.0): ").strip() or "0.1.0"

    if not title or not author:
        print("❗ Title and author are required.")
        return

    spec_id = generate_spec_id(title, author, version)
    print("hash_id: " + spec_id)


if __name__ == "__main__":
    main()
