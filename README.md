# 📉 Mistake Tracker

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-FF6B6B?style=for-the-badge)](https://github.com/ThanhNguyxn/Mistake-Tracker/pulls)

[![Tests](https://img.shields.io/github/actions/workflow/status/ThanhNguyxn/Mistake-Tracker/ci.yml?branch=main&label=Tests&style=flat-square&logo=github)](https://github.com/ThanhNguyxn/Mistake-Tracker/actions)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-orange?style=flat-square)](https://github.com/astral-sh/ruff)
[![Type Checked](https://img.shields.io/badge/type%20checked-mypy-blue?style=flat-square)](https://mypy-lang.org/)
[![codecov](https://img.shields.io/codecov/c/github/ThanhNguyxn/Mistake-Tracker?style=flat-square&logo=codecov)](https://codecov.io/gh/ThanhNguyxn/Mistake-Tracker)

**🎯 Track your learning mistakes. Identify weak points. Improve efficiently.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

---

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="100" />

</div>

---

## ✨ Features

<table>
<tr>
<td>

### 📝 **Log Mistakes**
Record subject, error description, and solution with automatic timestamps.

### 📊 **Smart Analytics**
View error breakdown and percentage by subject to identify weak points.

### 🔍 **Search & Filter**
Find mistakes quickly with keyword search across all entries.

</td>
<td>

### ✏️ **Edit & Delete**
Modify or remove entries when needed with confirmation prompts.

### 💾 **Auto-Backup**
Data is saved instantly with automatic backup rotation (20 versions).

### 📄 **Pagination**
Browse through large datasets with paginated view (10 items/page).

</td>
</tr>
</table>

---

## 🚀 Installation

### Option 1: Quick Start

```bash
# Clone the repository
git clone https://github.com/ThanhNguyxn/Mistake-Tracker.git
cd Mistake-Tracker

# Run directly
python -m mistake_tracker
```

### Option 2: Install as Package

```bash
# Install in editable mode
pip install -e .

# Run from anywhere
mistake-tracker
```

### Option 3: Development Setup

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Setup pre-commit hooks
pre-commit install

# Run tests
pytest tests/ -v
```

---

## 📖 Usage

### Menu Options

| Option | Icon | Description |
|--------|------|-------------|
| **1** | ➕ | Add a new mistake with subject, description, and fix |
| **2** | 📋 | View all mistakes with statistics and filtering |
| **3** | ✏️ | Edit or delete existing entries |
| **4** | 🚪 | Exit the program safely |

### Example Session

```
╔══════════════════════════════════════╗
║       📉 MISTAKE TRACKER             ║
╠══════════════════════════════════════╣
║  [1] ➕ Add New Mistake              ║
║  [2] 📋 View Mistakes                ║
║  [3] ✏️  Edit/Delete                  ║
║  [4] 🚪 Exit                         ║
╚══════════════════════════════════════╝

Choose (1-4): 2

📊 Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Mistakes: 15

Subject          │ Count │ Rate
─────────────────┼───────┼───────
Math             │ 10    │ 66.7%
English          │ 3     │ 20.0%
Coding           │ 2     │ 13.3%
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core language |
| ![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) | Testing framework |
| ![Ruff](https://img.shields.io/badge/-Ruff-D7303C?style=flat-square&logo=ruff&logoColor=white) | Linting & formatting |
| ![Mypy](https://img.shields.io/badge/-Mypy-2A6DB2?style=flat-square&logo=python&logoColor=white) | Type checking |
| ![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white) | CI/CD |

---

## 📂 Project Structure

```
Mistake-Tracker/
├── 📁 src/
│   └── 📁 mistake_tracker/
│       ├── __init__.py      # Package init
│       ├── __main__.py      # Entry point
│       ├── cli.py           # CLI interface
│       └── data.py          # Data management
├── 📁 tests/
│   └── test_tracker.py      # Unit tests
├── 📁 .github/
│   └── 📁 workflows/
│       └── ci.yml           # GitHub Actions CI
├── pyproject.toml           # Project config
├── ruff.toml                # Linter config
├── .pre-commit-config.yaml  # Pre-commit hooks
└── README.md                # Documentation
```

---

## 🤝 Contributing

Contributions are welcome! Please check out our [Contributing Guide](CONTRIBUTING.md).

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/amazing`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing`)
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ by [Minx-nie](https://github.com/minx-nie)**

[![Star](https://img.shields.io/github/stars/ThanhNguyxn/Mistake-Tracker?style=social)](https://github.com/ThanhNguyxn/Mistake-Tracker/stargazers)
[![Fork](https://img.shields.io/github/forks/ThanhNguyxn/Mistake-Tracker?style=social)](https://github.com/ThanhNguyxn/Mistake-Tracker/network/members)

</div>