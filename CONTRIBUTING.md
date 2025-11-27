# 🤝 Contributing to Monodoc

Welcome! We're thrilled you're interested in contributing to Monodoc — a unified documentation platform for multi-repo, multi-branch ecosystems.

Whether you're fixing a typo, improving docs, adding features, or reporting bugs — your help makes Monodoc better for everyone ✨

## 🛠️ Local Development Setup

We use uv for fast, reproducible Python tooling & dependency management.

```sh
# Clone this repo
git clone https://github.com/hf-xz/monodoc.git
cd monodoc

# Install dependencies with uv
uv sync --dev

# Verify installation
uv run monodoc --help

# Optional: Activate the venv (created by uv at .venv/)
source .venv/bin/activate  # Linux/macOS
# or
.venv\bin\activate.bat     # Windows (PowerShell: `.venv\bin\activate.ps1`)
# then
monodoc --help
```
