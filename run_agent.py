from agent.loop import fix_repo
from agent.tools import run_tests

repo = "buggy_repos/repo_03"

print("BEFORE:")
print(run_tests(repo))

print("ROBOT SAYS:")
print(fix_repo(repo))

print("AFTER:")
print(run_tests(repo))