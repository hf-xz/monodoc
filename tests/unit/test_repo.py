"""
tests.unit.test_repo
--------------------
Unit tests for the monodoc.core.sync.repo module.
"""

from monodoc.core.sync.repo import get_name_from_URL


def test_get_name_from_URL():
    # "input URL", "expected repo name"
    test_cases = [
        ("git@github.com:user/repo.git", "repo"),
        ("git@gitlab.com:group/subgroup/project.git", "project"),
        ("https://github.com/user/repo.git", "repo"),
        ("http://github.com/user/repo.git", "repo"),
        ("https://gitlab.com/group/subgroup/project.git", "project"),
        ("git://github.com/user/repo.git", "repo"),
        ("ssh://git@github.com/user/repo.git", "repo"),
        ("ssh://user@server.com:2222/path/to/repo.git", "repo"),
        ("file:///home/user/repo.git", "repo"),
        ("file://localhost/path/to/repo.git", "repo"),
        ("/home/user/repo.git", "repo"),
        ("./local/repo.git", "repo"),
        ("../parent/repo.git", "repo"),
        ("~/my-repo.git", "my-repo"),
        ("https://github.com/user/repo", "repo"),  # without .git
        ("git@host:user/repo-name.git", "repo-name"),
        ("git@host:user/repo_name.git", "repo_name"),
    ]
    for url, expected_name in test_cases:
        assert get_name_from_URL(url) == expected_name
