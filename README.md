# monodoc™

> **One portal. Every branch. Instant search.**
>
> A unified documentation platform for multi-repo, multi-branch ecosystems.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![Status: Pre-Alpha](https://img.shields.io/badge/status-pre--alpha-orange)

🔍 Search across repositories, branches, and versions — all from a single interface.

📦 Self-hosted, extensible, and built for developer workflows.

---

## ✨ Why monodoc?

| Problem                              | monodoc Solution                           |
| ------------------------------------ | ------------------------------------------ |
| Docs scattered across repos/branches | → **Unified view** in one portal           |
| Can’t search across versions         | → **Cross-branch full-text search**        |
| Manual sync & indexing               | → **Git-native sync** (webhook, CI, local) |
| Lock-in to vendor tools              | → **Open core**, self-hosted, extensible   |

---

## 🧩 Architecture

The system follows a modular design with decoupled components:

- **Interface Layer**: HTTP API and CLI
- **Core Services**: `sync`, `search`, `storage`, `cache`
- **Search Backend**: Pluggable via abstraction layer
- **Data Sources**: Git repositories (GitHub, GitLab, self-hosted)

![architecture](docs/assets/architecture.drawio.svg)

---

## 🌐 Roadmap

This project is currently at the MVP (Minimum Viable Product) stage.

The overall roadmap is:

- [ ] Implement `core.sync`, be able to use `api` and `cli` to call one-time sync.
- [ ] Implement polling and webhook sync strategy.
- [ ] Implement `core.search`, `core.storage` and `core.cache`.
  - [ ] Implement simple built-in components.
  - [ ] Provide adapter layer for different backends.
- [ ] Implement `ui`, `api`, `cli` and ready to go online.
- [ ] Introduce AI-powered features.
  - [ ] Semantic search via embedding (e.g., BGE) + vector DB
  - [ ] RAG-based Q&A with local LLM (e.g., Qwen/Ollama)
  - [ ] Auto-tagging & change impact analysis

## 📬 Questions

Open an [issue](https://github.com/hf-xz/monodoc/issues) — we reply fast!
