# 🤖 CodePilot AI

> **An AI Software Engineering Agent built with LangGraph, Ollama, RAG, ChromaDB, and Gradio.**

CodePilot AI is an autonomous AI software engineering assistant that understands an existing codebase, plans implementations, generates code, reviews AI-generated changes, and safely applies them through Git automation.

Instead of generating isolated code snippets, CodePilot AI performs **repository-level reasoning** using Retrieval-Augmented Generation (RAG), enabling it to understand project structure and generate context-aware code modifications.

---

# ✨ Features

## 🧠 Repository Intelligence

* 📁 Repository Analysis
* 🌿 Git Repository Detection
* 📦 Dependency Detection
* 🏗️ Framework Detection
* 📖 README Parsing
* 📊 Repository Statistics
* 🧭 Entry Point Detection

---

## 🔍 Retrieval-Augmented Generation (RAG)

* Intelligent Code Chunking
* ChromaDB Vector Store
* Ollama Embeddings
* Semantic Code Retrieval
* Repository Context Building
* Context-Aware Prompt Construction

---

## 🤖 AI Software Engineering Workflow

* Repository Analysis
* Codebase Indexing
* Semantic Retrieval
* Execution Planning
* AI Code Generation
* AI Code Review
* Automatic Retry Loop
* Human Approval
* Safe Code Application

---

## 🌿 Git Automation

* Git Repository Detection
* Branch Detection
* Automatic File Writing
* Git Stage
* AI Commit Message Generation
* Automatic Git Commit

---

## 🖥️ Interactive Dashboard

* 📋 Execution Plan
* 💻 Generated Files
* 🔍 AI Review
* 🌿 Git Information
* 📄 Final Report
* 📜 Workflow Logs

---

# 🛠️ Tech Stack

| Category        | Technology  |
| --------------- | ----------- |
| Language        | Python      |
| Workflow        | LangGraph   |
| LLM             | Ollama      |
| Embeddings      | Nomic Embed |
| RAG             | LangChain   |
| Vector Database | ChromaDB    |
| UI              | Gradio      |
| Git             | GitPython   |
| Data Models     | Pydantic    |
| Testing         | Pytest      |

---

# 🏗️ System Architecture

```text
                     User
                       │
                       ▼
                Gradio Dashboard
                       │
                       ▼
              LangGraph Workflow
                       │
 ┌──────────────┬──────────────┬──────────────┐
 ▼              ▼              ▼              ▼
Analyzer     Retriever      Planner      Generator
                                         │
                                         ▼
                                   Reviewer
                                         │
                                         ▼
                                 Final Report
                                         │
                                 Human Approval
                                         │
                                         ▼
                                   Apply Changes
                                         │
              ┌──────────────────────────┴─────────────────────────┐
              ▼                                                    ▼
         File Writer                                         Git Automation
                                                             │
                                                   Stage → Commit Message → Commit
```

---

# 🔄 Workflow

```text
User Task
      │
      ▼
Repository Analysis
      ▼
Repository Indexing
      ▼
Semantic Retrieval (RAG)
      ▼
Execution Planning
      ▼
Code Generation
      ▼
AI Code Review
      │
      ├── Approved
      │        ▼
      │   Final Report
      │        ▼
      │ Human Approval
      │        ▼
      │ Apply Changes
      │        ▼
      │ Git Commit
      │
      └── Retry (up to 3 attempts)
```

---

# 📂 Project Structure

```text
CodePilot-AI/
│
├── config/
├── graph/
│   ├── nodes/
│   ├── router.py
│   ├── state.py
│   └── workflow.py
│
├── models/
├── services/
│   ├── generator/
│   ├── planner/
│   ├── repository/
│   ├── reviewer/
│   ├── git/
│   ├── indexing/
│   ├── report/
│   └── writer/
│
├── ui/
├── tests/
├── storage/
├── pyproject.toml
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/barathwaj-rs/CodePilot-AI.git

cd CodePilot-AI
```

Install dependencies

```bash
uv sync
```

Start Ollama

```bash
ollama serve
```

Pull the required models

```bash
ollama pull qwen3:latest
ollama pull nomic-embed-text
```

Launch CodePilot AI

```bash
uv run python -m ui.app
```

---

# 🖥️ Dashboard

The Gradio dashboard provides:

* Execution Plan
* Generated Files
* AI Review
* Git Information
* Final Report
* Workflow Logs

> *(Add screenshots here after uploading them to the repository.)*

---

# 📈 Project Status

| Module              | Status |
| ------------------- | ------ |
| Repository Analysis | ✅      |
| RAG Pipeline        | ✅      |
| Planner             | ✅      |
| Generator           | ✅      |
| Reviewer            | ✅      |
| Retry Workflow      | ✅      |
| Writer              | ✅      |
| Git Integration     | ✅      |
| Dashboard           | ✅      |
| Workflow Logs       | ✅      |

---

# 🚀 Roadmap

## Version 1.1

* Side-by-side Diff Viewer
* Apply Selected Files
* Automatic Formatting
* Linting
* Test Execution

## Version 2.0

* Pull Request Creation
* Docker Support
* VS Code Extension
* Multi-Agent Collaboration
* Multi-LLM Support
* GitHub Actions Integration

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork the repository and submit a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Barathwaj R S**

B.Tech CSE (AI & DS)

SASTRA Deemed University
