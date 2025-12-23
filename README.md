# 📉 Mistake Tracker

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Tests](https://img.shields.io/github/actions/workflow/status/minx-nie/Mistake-Tracker/ci.yml?branch=main&label=Tests&style=for-the-badge&logo=github)](https://github.com/minx-nie/Mistake-Tracker/actions)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-FF6B6B?style=for-the-badge)](https://github.com/minx-nie/Mistake-Tracker/pulls)

<br/>

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark" width="120" />

**🎯 Track your learning mistakes. Identify weak points. Improve efficiently.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📝 Log Mistakes
Record subject, error description, and solution with automatic timestamps.

### 📊 Smart Analytics
View error breakdown and percentage by subject to identify weak points.

### 🔍 Search & Filter
Find mistakes quickly with keyword search across all entries.

</td>
<td width="50%">

### ✏️ Edit & Delete
Modify or remove entries when needed with confirmation prompts.

### � Auto-Backup
Data is saved instantly with automatic backup rotation (20 versions).

### � Pagination
Browse through large datasets with paginated view (10 items/page).

</td>
</tr>
</table>

---

## 🚀 Installation

### Option 1: Quick Start

```bash
# Clone the repository
git clone https://github.com/minx-nie/Mistake-Tracker.git
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

### Main Menu

When you run the program, you'll see this menu:

```
╔══════════════════════════════════════╗
║       📉 MISTAKE TRACKER             ║
╠══════════════════════════════════════╣
║  [1] ➕ Add New Mistake              ║
║  [2] 📋 View Mistakes                ║
║  [3] ✏️  Edit/Delete                 ║
║  [4] 🚪 Exit                         ║
╚══════════════════════════════════════╝

Choose (1-4):
```

---

### 1️⃣ Add New Mistake

Select `1` → Enter the details:

```
━━━ ➕ Add New Mistake ━━━
Subject: math
Mistake: Wrong formula for area calculation
Fix: S = pi * r^2, not 2*pi*r

✅ Mistake added successfully!
```

---

### 2️⃣ View Mistakes & Statistics

Select `2` → See statistics and list:

```
━━━ 📋 View Mistakes ━━━
🔍 Filter by keyword (Enter to skip):

📊 Statistics (Total: 15)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subject              │ Count │  Rate
─────────────────────┼───────┼───────
Math                 │    10 │ 66.7%
English              │     3 │ 20.0%
Coding               │     2 │ 13.3%

📝 All Mistakes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Math] Wrong formula → S = pi*r^2 (2024-12-23)
2. [Math] Sign error → Check steps again (2024-12-22)
...
```

> 💡 **Tip:** Enter a keyword to filter mistakes by subject, description, or fix.

---

### 3️⃣ Edit or Delete

Select `3` → Choose entry number → `e` to edit or `d` to delete:

```
━━━ ✏️ Edit/Delete ━━━
1. [Math] Wrong formula
2. [English] Grammar mistake

Choose number (0 = cancel): 1
(e)dit / (d)elete: e

💡 Leave blank to keep current value.
Subject [math]:
Mistake [Wrong formula]: Wrong volume formula
Fix [S = pi*r^2]: V = 4/3 * pi * r^3

✅ Updated.
```

---

### 4️⃣ Exit

Select `4` to safely exit the program. Your data is automatically saved!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core language (3.9+) |
| ![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) | Testing framework |
| ![Ruff](https://img.shields.io/badge/-Ruff-D7303C?style=flat-square&logo=ruff&logoColor=white) | Linting & formatting |
| ![Mypy](https://img.shields.io/badge/-Mypy-2A6DB2?style=flat-square&logo=python&logoColor=white) | Type checking |
| ![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white) | CI/CD |

---

## 📂 Project Structure

```
Mistake-Tracker/
├── 📁 src/mistake_tracker/
│   ├── __init__.py      # Package init
│   ├── __main__.py      # Entry point
│   ├── cli.py           # CLI interface
│   └── data.py          # Data management
├── 📁 tests/
│   └── test_tracker.py  # Unit tests
├── 📁 .github/workflows/
│   └── ci.yml           # GitHub Actions CI
├── pyproject.toml       # Project config
├── ruff.toml            # Linter config
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

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

[![Star](https://img.shields.io/github/stars/minx-nie/Mistake-Tracker?style=social)](https://github.com/minx-nie/Mistake-Tracker/stargazers)
[![Fork](https://img.shields.io/github/forks/minx-nie/Mistake-Tracker?style=social)](https://github.com/minx-nie/Mistake-Tracker/network/members)

</div>