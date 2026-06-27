# 🚀 CodePilot AI

> **An AI Software Engineering Agent built with LangGraph, RAG, Ollama, and ChromaDB.**

CodePilot AI is an agentic software engineering assistant designed to understand, analyze, and modify software repositories using Large Language Models (LLMs). Instead of working with isolated code snippets, it builds a semantic understanding of an entire codebase using Retrieval-Augmented Generation (RAG), enabling repository-level reasoning and intelligent code assistance.

The long-term vision of CodePilot AI is to provide an end-to-end AI software engineering workflow that can:

* Analyze repositories
* Understand project architecture
* Plan implementation strategies
* Generate code changes
* Review generated code
* Assist developers throughout the software development lifecycle

> **Project Status:** 🚧 Active Development (v0.5)

---

# ✨ Features

## Repository Intelligence

* 📁 Repository tree analysis
* 🌐 Programming language detection
* 🏗️ Framework detection
* 📦 Dependency analysis
* 🚪 Entry point detection
* 📖 README parsing
* 🌿 Git repository analysis
* 📊 Repository statistics

---

## Retrieval-Augmented Generation (RAG)

* ✂️ Intelligent code chunking
* 🧠 Local embedding generation
* 🗂️ ChromaDB vector storage
* 🔍 Semantic code retrieval
* 🧩 Repository context building
* 📚 Repository-specific vector collections

---

## AI Workflow

* 🔄 LangGraph workflow orchestration
* 🧱 Typed workflow state
* 🗃️ Repository context management
* 📋 Execution planning (In Progress)

---

## Software Engineering

* 🧩 Modular architecture
* ⚙️ Centralized configuration
* 🧪 Unit testing
* 📝 Structured models
* 🔌 Extensible service design

---

# 🛠️ Tech Stack

| Category        | Technology        |
| --------------- | ----------------- |
| Language        | Python            |
| Workflow        | LangGraph         |
| LLM             | Ollama            |
| Embeddings      | Ollama Embeddings |
| RAG Framework   | LangChain         |
| Vector Database | ChromaDB          |
| UI              | Gradio            |
| Git Integration | GitPython         |
| Configuration   | python-dotenv     |
| Testing         | Python Unit Tests |


# 🏗️ System Architecture

CodePilot AI is organized into modular layers to separate responsibilities and make the system easy to extend.

```text
                        User
                          │
                          ▼
                    Gradio Interface
                          │
                          ▼
                 Workflow Controller
                          │
                          ▼
                     LangGraph Engine
                          │
      ┌───────────────────┼───────────────────┐
      ▼                   ▼                   ▼
 Repository Analyzer   Context Builder    Future AI Agents
      │                   │                   │
      ▼                   ▼                   ▼
Repository Analysis  Repository Context  Planner / Generator / Reviewer
                          │
                          ▼
                    Final AI Response
```

---

# 🧠 AI Workflow

The overall execution flow of CodePilot AI is:

```text
User Task
    │
    ▼
Clone Repository
    │
    ▼
Repository Analysis
    │
    ▼
Repository Indexing
    │
    ▼
Semantic Retrieval (RAG)
    │
    ▼
Context Building
    │
    ▼
Planner (Upcoming)
    │
    ▼
Generator (Upcoming)
    │
    ▼
Reviewer (Upcoming)
    │
    ▼
Final Response
```

---

# 📂 Project Structure

```text
CodePilot-AI/
│
├── config/             # Configuration and logging
├── controllers/        # Application controllers
├── docs/               # Project documentation
├── graph/              # LangGraph workflow
├── models/             # Shared data models
├── prompts/            # Prompt templates
├── services/
│   ├── indexing/       # RAG indexing pipeline
│   ├── planner/        # Planning agent
│   ├── rag/            # Context builder
│   ├── repository/     # Repository intelligence
│   ├── generator/      # Code generation agent (planned)
│   └── reviewer/       # Code review agent (planned)
│
├── storage/            # Chroma database & repositories
├── tests/              # Unit tests
├── main.py
└── README.md
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone <repository-url>
cd CodePilot-AI
```

## Install dependencies

```bash
uv sync
```

## Configure environment

Create a `.env` file.

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3:latest
```

## Start Ollama

```bash
ollama serve
```

Pull the model if needed:

```bash
ollama pull qwen3:latest
```

---

# 🚀 Run

Launch the Gradio interface.

```bash
uv run main.py
```

The application will be available at:

```
http://127.0.0.1:7860
```


# 🗺️ Development Roadmap

CodePilot AI is being developed in multiple phases.

| Version  | Status         | Features                               |
| -------- | -------------- | -------------------------------------- |
| **v0.1** | ✅ Completed    | Project Foundation, LangGraph Workflow |
| **v0.2** | ✅ Completed    | Repository Analysis Engine             |
| **v0.3** | ✅ Completed    | RAG Engine & Semantic Code Search      |
| **v0.4** | ✅ Completed    | Infrastructure Refactoring             |
| **v0.5** | ✅ Completed    | Documentation & Project Architecture   |
| **v0.6** | 🚧 In Progress | Planner Agent                          |
| **v0.7** | ⏳ Planned      | Generator Agent                        |
| **v0.8** | ⏳ Planned      | Reviewer Agent                         |
| **v0.9** | ⏳ Planned      | Git Integration                        |
| **v1.0** | 🎯 Goal        | Complete AI Software Engineering Agent |

---

# 🚀 Future Features

The following features are planned for future releases.

### AI Agents

* Planner Agent
* Generator Agent
* Reviewer Agent
* Test Generation Agent
* Documentation Generation Agent

### Repository Intelligence

* Multi-language repository support
* Incremental indexing
* Repository caching
* Large repository optimization

### AI Capabilities

* Multi-LLM support
* Conversation memory
* Streaming responses
* Tool calling
* Function calling

### Developer Experience

* VS Code Extension
* FastAPI Backend
* Docker Support
* GitHub Pull Request Generation
* GitHub Actions Integration

---

# 📈 Current Progress

```text
Foundation                     ██████████ 100%
Repository Intelligence        ██████████ 100%
RAG Engine                     ██████████ 100%
Documentation                  █████████░  90%

Planner                        ░░░░░░░░░░   0%
Generator                      ░░░░░░░░░░   0%
Reviewer                       ░░░░░░░░░░   0%
Git Integration                ░░░░░░░░░░   0%
```

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

Please ensure all tests pass before submitting changes.

---

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.
