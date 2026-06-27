from models.repository_analysis import RepositoryAnalysis
from services.repository.tree_builder import TreeBuilder
from services.repository.language_detector import LanguageDetector
from services.repository.framework_detector import FrameworkDetector
from services.repository.dependency_parser import DependencyParser

class RepositoryAnalyzer:

    @staticmethod
    def analyze(repo_path: str) -> RepositoryAnalysis:

        files = TreeBuilder.build(repo_path)

        languages = LanguageDetector.detect(files)

        frameworks = FrameworkDetector.detect(
            repo_path,
            files
        )


        dependencies = DependencyParser.parse(
            repo_path,
            files,
        )

        analysis = RepositoryAnalysis(
            files=files,
            languages=languages,
            frameworks=frameworks,
            dependencies=dependencies,
        )

        return analysis