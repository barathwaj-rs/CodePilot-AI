from models.repository_analysis import RepositoryAnalysis
from models.repository_context import RepositoryContext
from models.retrieved_chunk import RetrievedChunk
from services.planner.planner import Planner


def main():

    analysis = RepositoryAnalysis(
        files=["auth.py", "routes.py"],
        languages={"Python": 2},
        frameworks=["FastAPI"],
        dependencies={
            "Python": [
                "fastapi",
                "pydantic",
            ]
        },
        entry_points=["main.py"],
    )

    chunks = [
        RetrievedChunk(
            file="auth.py",
            content="""
def login():
    pass
""",
            score=0.12,
        ),
        RetrievedChunk(
            file="routes.py",
            content="""
@app.get("/")
def home():
    pass
""",
            score=0.25,
        ),
    ]

    context = RepositoryContext(
        analysis=analysis,
        retrieved_chunks=chunks,
        user_task="Add JWT Authentication",
    )

    planner = Planner()

    plan = planner.plan(context)

    print(plan)


if __name__ == "__main__":
    main()