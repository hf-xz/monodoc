"""
monodoc.core.sync.repo
----------------------
This module provides high-level functions for managing Git repositories,
including initialization and cloning. It leverages the `git_utils` module
to perform low-level Git operations, ensuring a clean separation of concerns
and promoting code reuse.
"""

import re
from pathlib import Path
from urllib.parse import urlparse

from pydantic import BaseModel, FilePath, field_validator


class Repo(BaseModel):
    """
    A class representing a Git repository.
    """

    name: str  # name of the repository
    path: FilePath  # file system path to the repository
    remote_url: str  # remote URL of the repository
    synced_branches: list[str]  # list of synconized branch names

    @field_validator("remote_url")
    @classmethod
    def validate_git_remote(cls, v: str):
        patterns = [
            # SSH format: git@host:user/repo.git
            r"^[\w-]+@[\w.-]+:[\w./-]+\.git$",
            # HTTPS/HTTP
            r"^https?://[\w.-]+/[\w./-]+\.git$",
            r"^https?://[\w.-]+/[\w./-]+$",
            # Git Protocol
            r"^git://[\w.-]+/[\w./-]+\.git$",
            # SSH Protocol
            r"^ssh://[\w-]+@[\w.-]+/[\w./-]+\.git$",
            # Local paths
            r"^(\.?\.?/|/|~)[\w./-]+(\.git)?$",
            # Local file URLs
            r"^file:///[\w./-]+(\.git)?$",
        ]

        # 检查是否匹配任一模式
        for pattern in patterns:
            if re.match(pattern, v):
                return v

        raise ValueError(f"Invalid Git remote URL format: {v}")


def get_name_from_URL(url: str) -> str:
    """
    Extracts the repository name from a given Git remote URL.

    Args:
        url (str): The Git remote URL.
    Returns:
        str: The extracted repository name.
    Examples:
        >>> get_name_from_URL('git@github.com:hf-xz/monodoc.git')
        >>> get_name_from_URL('https://github.com/hf-xz/monodoc.git')
        'monodoc'
    """
    if not url:
        return ""

    # remove .git suffix
    if url.endswith(".git"):
        url = url[:-4]

    # try to parse URL
    if "://" in url:
        parsed = urlparse(url)
        path = parsed.path
    else:
        path = url

    # handle SSH format: git@host:path
    if "@" in url and ":" in url and "://" not in url:
        # git@github.com:user/repo
        parts = url.split(":", 1)
        if len(parts) > 1:
            path = parts[1]

    # remove leading/trailing slashes
    path = path.strip("/")

    parts = [p for p in path.split("/") if p]
    if not parts:
        return ""

    return parts[-1]


class RepoManager:
    """
    A manager class for handling Git repository operations.
    """

    def __init__(self, repo_list: list[Repo]):
        self.repo_list = repo_list

    def init_repo(self, path: Path, remote_url: str, name: str = "") -> bool:
        """
        Initializes a new Git repository at the specified path and sets the remote URL.

        Args:
            path (str): The directory path where the repository will be initialized.
            remote_url (str): The URL of the remote repository.

        Returns:
            bool: True if the repository was initialized, False otherwise.

        Examples:
            >>> success = RepoManager.init_repo('/path/to/repo', 'url')
        """
        from monodoc.core.sync.git_utils import add_remote, init_repo, is_repo

        name = name.strip()
        if not name:
            name = get_name_from_URL(remote_url)

        try:
            new_repo = Repo(name=name, path=path, remote_url=remote_url, synced_branches=[])

            if is_repo(path):
                raise Exception("The specified path is already a Git repository.")

            init_repo(path)
            add_remote(path, "origin", remote_url)
            self.repo_list.append(new_repo)

            return True

        except Exception as e:
            print(f"Failed to create Repo instance: {e}")

            return False
