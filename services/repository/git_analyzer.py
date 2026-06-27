from git import Repo


class GitAnalyzer:
    """
    Reads Git repository information.
    """

    @staticmethod
    def analyze(repo_path: str) -> dict:

        repo = Repo(repo_path)

        return {
            "repository": repo.working_tree_dir.split("\\")[-1],
            "branch": repo.active_branch.name,
            "last_commit": repo.head.commit.hexsha[:8],
            "last_message": repo.head.commit.message.strip(),
            "author": repo.head.commit.author.name,
            "remote": (
                repo.remotes.origin.url
                if repo.remotes
                else ""
            ),
        }