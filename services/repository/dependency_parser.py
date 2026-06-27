import tomllib
from pathlib import Path


class DependencyParser:

    @staticmethod
    def parse(repo_path: str, files: list[str]) -> dict[str, list[str]]:

        root = Path(repo_path)

        dependencies = {}

        if "pyproject.toml" in files:
            dependencies["Python"] = DependencyParser.parse_pyproject(
                root / "pyproject.toml"
            )

        if "requirements.txt" in files:
            dependencies["Python"] = DependencyParser.parse_requirements(
                root / "requirements.txt"
            )

        return dependencies

    @staticmethod
    def parse_pyproject(path: Path) -> list[str]:

        with open(path, "rb") as f:
            data = tomllib.load(f)

        project = data.get("project", {})

        dependencies = project.get("dependencies", [])

        packages = []

        for dependency in dependencies:

            package = (
                dependency
                .split(">=")[0]
                .split("==")[0]
                .split("<=")[0]
                .strip()
            )

            packages.append(package)

        return sorted(packages)

    @staticmethod
    def parse_requirements(path: Path) -> list[str]:

        packages = []

        with open(path, encoding="utf-8") as f:

            for line in f:

                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                package = (
                    line
                    .split(">=")[0]
                    .split("==")[0]
                    .split("<=")[0]
                    .strip()
                )

                packages.append(package)

        return sorted(packages)