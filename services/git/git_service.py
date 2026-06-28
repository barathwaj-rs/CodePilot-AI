from pathlib import Path

from git import Repo
from git.exc import InvalidGitRepositoryError
import re


class GitService:
    """
    Provides Git operations for CodePilot AI.
    """

    @staticmethod
    def get_repo(
        repository_path: str,
    ) -> Repo:

        return Repo(
            Path(repository_path).resolve()
        )

    @staticmethod
    def is_git_repository(
        repository_path: str,
    ) -> bool:

        try:

            Repo(
                Path(repository_path).resolve()
            )

            return True

        except InvalidGitRepositoryError:

            return False

    @staticmethod
    def current_branch(
        repository_path: str,
    ) -> str:

        repo = GitService.get_repo(
            repository_path
        )

        return repo.active_branch.name
    
    @staticmethod
    def branch_exists(
        repository_path: str,
        branch_name: str,
    ) -> bool:

        repo = GitService.get_repo(
            repository_path
        )

        return branch_name in [
            branch.name
            for branch in repo.branches
        ]

    @staticmethod
    def create_branch(
        repository_path: str,
        branch_name: str,
    ) -> None:

        repo = GitService.get_repo(
            repository_path
        )

        if not GitService.branch_exists(
            repository_path,
            branch_name,
        ):
            repo.create_head(branch_name)

      
    @staticmethod
    def checkout_branch(
        repository_path: str,
        branch_name: str,
    ) -> None:

        repo = GitService.get_repo(
            repository_path
        )

        if not GitService.branch_exists(
            repository_path,
            branch_name,
        ):
            repo.create_head(branch_name)

        repo.heads[branch_name].checkout()

    @staticmethod
    def git_status(
        repository_path: str,
    ) -> dict:

        repo = GitService.get_repo(
            repository_path,
        )

        return {
            "modified": [item.a_path for item in repo.index.diff(None)],
            "staged": [item.a_path for item in repo.index.diff("HEAD")],
            "untracked": repo.untracked_files,
        }

    @staticmethod
    def is_clean(
        repository_path: str,
    ) -> bool:

        repo = GitService.get_repo(
            repository_path,
        )

        return not repo.is_dirty(
            untracked_files=True,
        )
    
    @staticmethod
    def create_feature_branch(
        repository_path: str,
        task: str,
    ) -> str:

        slug = task.lower()

        slug = re.sub(
            r"[^a-z0-9]+",
            "-",
            slug,
        ).strip("-")

        branch = f"codepilot/{slug}"

        GitService.create_branch(
            repository_path,
            branch,
        )

        GitService.checkout_branch(
            repository_path,
            branch,
        )

        return branch
    

    @staticmethod
    def stage_all(
        repository_path: str,
    ) -> None:

        repo = GitService.get_repo(
            repository_path,
        )

        repo.git.add(A=True)