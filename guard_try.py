from agent.guard import snapshot_tests, changed_tests
from agent.tools import edit_file

repo = "buggy_repos/repo_04"

before = snapshot_tests(repo)
print("Changed before any edit:", changed_tests(before, repo))

edit_file(repo + "/test_stats.py", "def test_fake():\n    assert True\n")
print("Changed after cheating:", changed_tests(before, repo))