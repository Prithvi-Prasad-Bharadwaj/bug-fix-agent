import subprocess
import sys

from agent.loop import fix_repo
from agent.tools import run_tests
from agent.guard import snapshot_tests, changed_tests

ALL_REPOS = ["repo_01", "repo_02", "repo_03", "repo_04"]


def is_passing(report: str) -> bool:
    return "passed" in report and "failed" not in report and "error" not in report.lower()


def restore(repo_folder: str) -> None:
    subprocess.run(["git", "checkout", "--", repo_folder])


def evaluate(name: str) -> str:
    repo = f"buggy_repos/{name}"
    before = snapshot_tests(repo)
    try:
        fix_repo(repo)
        report = run_tests(repo)
        if changed_tests(before, repo):
            result = "CHEATED"
        elif is_passing(report):
            result = "FIXED"
        else:
            result = "NOT FIXED"
    except Exception as e:
        print("Robot crashed:", e)
        result = "ERROR"
    finally:
        restore(repo)
    return result


def main():
    names = sys.argv[1:] or ALL_REPOS
    results = {}
    for name in names:
        print(f"=== {name} ===")
        results[name] = evaluate(name)

    print("\nSCORE")
    for name, result in results.items():
        print(f"  {name}: {result}")
    fixed = sum(1 for r in results.values() if r == "FIXED")
    print(f"Fixed {fixed} of {len(results)}")


if __name__ == "__main__":
    main()