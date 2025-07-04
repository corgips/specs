import os
import re
import yaml

SPEC_DIR = "./specs"
VALID_HANDLE = re.compile(r"^@([a-z0-9.-]+)$")
VALID_HASH_ID = re.compile(r"^spec:[a-f0-9]{8}$")

required_fields = ["id", "hash_id", "title", "authors", "status", "created", "version"]


def validate_metadata(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return False, f"Missing YAML frontmatter in {filepath}"

    parts = content.split("---")
    if len(parts) < 3:
        return False, f"Malformed YAML frontmatter in {filepath}"

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return False, f"YAML parse error in {filepath}: {e}"

    missing = [field for field in required_fields if field not in meta]
    if missing:
        return False, f"Missing fields in {filepath}: {', '.join(missing)}"

    if not isinstance(meta["authors"], list):
        return False, f"'authors' must be a list in {filepath}"

    for handle in meta["authors"]:
        if not VALID_HANDLE.match(handle):
            return False, f"Invalid author handle in {filepath}: {handle}"

    if not VALID_HASH_ID.match(meta["hash_id"]):
        return False, f"Invalid hash_id format in {filepath}: {meta['hash_id']}"

    return True, f"✓ {filepath} passed"


def main():
    print("🔍 Validating spec metadata...")
    files = [f for f in os.listdir(SPEC_DIR) if f.endswith(".md")]
    all_passed = True

    for fname in files:
        path = os.path.join(SPEC_DIR, fname)
        ok, msg = validate_metadata(path)
        print(msg)
        if not ok:
            all_passed = False

    if all_passed:
        print("\n✅ All specs passed validation.")
    else:
        print("\n❌ Validation failed. Please fix the issues above.")


if __name__ == "__main__":
    main()
