from pathlib import Path


def snapshot_tests(repo_folder: str) -> dict:
    """Return {file path: file text} for every test file in the repo."""
    snapshot = {}
    for path in Path(repo_folder).glob("test_*.py"):
        snapshot[str(path)] = path.read_text()
    return snapshot


def changed_tests(before: dict, repo_folder: str) -> list:
    """Return the test files that were edited, deleted or added since the snapshot."""
    after = snapshot_tests(repo_folder)
    names = set(before) | set(after)
    return [name for name in names if before.get(name) != after.get(name)]