"""
monodoc.core.sync.git_utils
---------------------------
This module contains a set of utility functions for performing common Git operations
(pure repository/worktree operation wrappers). The design goal is to provide
lightweight, reusable, and easily testable functions for invoking git behavior
in scripts or applications in a controlled manner.

This module may be replaced by a more comprehensive Git library in the future,
but for now it serves as a simple and effective way to interact with Git repositories
"""

import os
import subprocess


def is_repo(path: str) -> bool:
    """
    Checks if the given path is a Git repository.

    Args:
        path (str): The file system path to check.

    Returns:
        bool: True if the path is a Git repository, False otherwise.

    Examples:
        >>> is_repo('/path/to/repo')
        True
    """
    # 检查路径是否存在且包含 .git 目录
    return os.path.isdir(os.path.join(path, ".git"))


def init_repo(path: str) -> None:
    """
    Initializes a new Git repository at the specified path.

    Args:
        path (str): The directory path where the repository will be initialized.

    Returns:
        None: The function does not return any value.

    Examples:
        >>> init_repo('/path/to/repo')
    """
    if not os.path.exists(path):
        os.makedirs(path)
    subprocess.run(["git", "-C", path, "init"], check=True)


def clone_repo(path: str, url: str) -> None:
    """
    Clones a Git repository from the specified URL to the given path.

    Args:
        path (str): The directory path where the repository will be cloned.
        url (str): The URL of the Git repository to clone.

    Returns:
        None: The function does not return any value.

    Examples:
        >>> clone_repo('/path/to/repo', 'url')
    """
    subprocess.run(["git", "clone", url, path], check=True)


def add_remote(path: str, name: str, url: str) -> None:
    """
    Adds a new remote to the Git repository.

    Args:
        path (str): The path to the Git repository.
        name (str): The name of the remote.
        url (str): The URL of the remote.

    Returns:
        None: The function does not return any value.

    Examples:
        >>> add_remote('/path/to/repo', 'origin', 'https://github.com/user/repo.git')
    """
    subprocess.run(["git", "-C", path, "remote", "add", name, url], check=True)


def remove_remote(path: str, name: str) -> None:
    """
    Removes a remote from the Git repository.

    Args:
        path (str): The path to the Git repository.
        name (str): The name of the remote to remove.

    Returns:
        None: The function does not return any value.

    Examples:
        >>> remove_remote('/path/to/repo', 'origin')
    """
    subprocess.run(["git", "-C", path, "remote", "remove", name], check=True)


def delete_branch(path: str, name: str) -> None:
    """
    Deletes a branch in the Git repository.

    Args:
        path (str): The path to the Git repository.
        name (str): The name of the branch to delete.

    Returns:
        None: The function does not return any value.

    Examples:
        >>> delete_branch('/path/to/repo', 'feature-branch')
    """
    subprocess.run(["git", "-C", path, "branch", "-d", name], check=True)


def fetch(path: str, remote: str) -> None:
    """
    Fetches updates from the specified remote in the Git repository.

    Args:
        path (str): The path to the Git repository.
        remote (str): The name of the remote to fetch from.

    Returns:
        None: The function does not return any value.

    Examples:
        >>> fetch('/path/to/repo', 'origin')
    """
    subprocess.run(["git", "-C", path, "fetch", remote], check=True)


def pull(path: str, remote: str, branch: str) -> None:
    """
    Pulls updates from the specified remote and branch in the Git repository.

    Args:
        path (str): The path to the Git repository.
        remote (str): The name of the remote to pull from.
        branch (str): The name of the branch to pull.

    Returns:
        None: The function does not return any value.

    Examples:
        >>> pull('/path/to/repo', 'origin', 'main')
    """
    subprocess.run(["git", "-C", path, "pull", remote, branch], check=True)
