"""Verify the minimum development environment for the Week 1 lab."""

from __future__ import annotations

import subprocess
import sys
from importlib.metadata import PackageNotFoundError, version


def package_version(name: str) -> str:
    """Return an installed package version or fail with a useful message."""
    try:
        return version(name)
    except PackageNotFoundError as exc:
        raise RuntimeError(f"required package is not installed: {name}") from exc


def git_output(*args: str) -> str:
    """Run Git and return stripped standard output."""
    completed = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def main() -> None:
    """Print stable evidence and fail if any requirement is unavailable."""
    if sys.version_info < (3, 10):
        raise RuntimeError("Python 3.10 or newer is required")

    print(f"PYTHON={sys.version.split()[0]}")
    print(f"NUMPY={package_version('numpy')}")
    print(f"JUPYTER={package_version('jupyterlab')}")

    if git_output("rev-parse", "--is-inside-work-tree") != "true":
        raise RuntimeError("current directory is not a Git work tree")

    commits = int(git_output("rev-list", "--count", "HEAD"))
    if commits < 1:
        raise RuntimeError("the repository has no commits")
    print(f"GIT_COMMITS={commits}")


if __name__ == "__main__":
    main()

