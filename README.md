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

### 💾 Auto-Backup
Data is saved instantly with automatic backup rotation (20 versions).

### 📄 Pagination
Browse through large datasets with paginated view (10 items/page).

</td>
</tr>
</table>

---

## 🚀 Installation

### Option 1: Quick Start (Recommended)

```bash
# Step 1: Clone the repository
git clone https://github.com/minx-nie/Mistake-Tracker.git
cd Mistake-Tracker

# Step 2: Install the package
pip install -e .

# Step 3: Run the program
python -m mistake_tracker
```

> ⚠️ **Important:** You must run `pip install -e .` before using `python -m mistake_tracker`, otherwise you'll get "No module named mistake_tracker" error.

---

### Option 2: Run Without Installing

If you prefer not to install, run the standalone script directly:

```bash
git clone https://github.com/minx-nie/Mistake-Tracker.git
cd Mistake-Tracker

# Run standalone script (no install needed)
python Mistake_Tracker.py
```

---

### Option 3: Development Setup

```bash
git clone https://github.com/minx-nie/Mistake-Tracker.git
cd Mistake-Tracker

# Install with development dependencies
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
║  [3] ✏️  Edit/Delete                  ║
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
├── Mistake_Tracker.py   # Standalone script (legacy)
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
<<<<<<< HEAD

---

<a id="english"></a>

## 🇬🇧 English

### 📌 About

**Mistake Tracker** is a lightweight Python CLI tool designed to help students and self-learners track their learning mistakes. By recording and analyzing errors, you can identify weak points and improve efficiently.

**Key highlights:**

* **Simple & Fast**: Runs directly in the terminal with a clean ASCII interface.
* **Persistent Storage**: Data is automatically saved to `mistakes.json` with backup.
* **Smart Analytics**: Automatically calculates error rates by subject.
* **No Dependencies**: Uses only Python standard libraries.

---

### ✨ Features

* ✍️ **Log Mistakes**: Record subject, error description, and the solution.
* 📊 **Statistics**: View error breakdown and percentage by subject.
* 🖊 **Edit/Delete Mistakes**: Modify or remove mistakes if needed.
* 💾 **Auto-Save & Backup**: Data is saved instantly with a backup.
* 🕒 **Timestamping**: Automatically records the date of the error.
* 🔢 **Pagination**: View mistakes in pages when dataset is large.
---

### 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Minx-nie/Mistake-Tracker.git

# 2. Navigate to the folder
cd Mistake-Tracker

# 3. Run the tool
python Mistake_Tracker.py
```

---

### ▶️ Usage

| Option                       | Description                                  |
| ---------------------------- | -------------------------------------------- |
| `1. [+] Add a New Mistake`   | Input subject, mistake details, and fix.     |
| `2. [*] View Mistakes`       | Show total errors and statistical breakdown. |
| `3. [!] Edit/Delete Mistake` | Edit or delete existing mistakes.            |
| `4. [X] Exit`                | Close the program safely.                    |

---

### 🎨 Interface Preview

```text
=== [ Mistake Tracker ] ===
1. [+] Add a New Mistake
2. [*] View Mistakes
3. [!] Edit/Delete Mistake
4. [X] Exit

Choose an option (1-4): 2

--- [*] View Mistakes ---
Total mistakes recorded: 15

Mistakes by Subject:
Subject         | Total mistakes | Rate      
---------------------------------------------
Math            | 10             | 66.7%
English         | 3              | 20.0%
Coding          | 2              | 13.3%

--- All Mistakes (paginated) ---
1. [Math] Wrong formula -> Correct formula (22-12-2025)
2. [Math] Calculation error -> Check steps (22-12-2025)
...
Press Enter to see more...
```

---

### 📄 License

MIT License
Author: **minx-nie**

---

<a id="vietnamese"></a>

## 🇻🇳 Tiếng Việt

### 📌 Giới thiệu

**Mistake Tracker** là công cụ dòng lệnh (CLI) bằng Python giúp học sinh, sinh viên ghi lại các lỗi sai trong quá trình học tập. Việc theo dõi lỗi giúp bạn nhận ra điểm yếu để cải thiện kịp thời.

**Điểm nổi bật:**

* **Đơn giản & Nhanh**: Chạy trực tiếp trên terminal, giao diện ASCII thân thiện.
* **Lưu trữ tự động & Backup**: Dữ liệu được lưu vào file `mistakes.json` và có bản sao backup.
* **Thống kê thông minh**: Tự động tính toán tỷ lệ % lỗi sai theo từng môn.
* **Không cần cài đặt**: Chỉ sử dụng thư viện có sẵn của Python.

---

### ✨ Tính năng

* ✍️ **Ghi lỗi**: Nhập môn học, mô tả lỗi và cách khắc phục.
* 📊 **Thống kê**: Xem tổng số lỗi và tỷ lệ phần trăm theo môn.
* 🖊 **Sửa/Xóa lỗi**: Chỉnh sửa hoặc xóa các lỗi đã nhập.
* 💾 **Auto-Save & Backup**: Dữ liệu được lưu tức thì kèm backup.
* 🕒 **Thời gian**: Tự động lưu ngày tháng khi ghi lỗi.
* 🔢 **Phân trang**: Xem lỗi theo trang khi dữ liệu lớn.

---

### 🚀 Cài đặt & Chạy

```bash
# 1. Tải source code về
git clone https://github.com/Minx-nie/Mistake-Tracker.git

# 2. Vào thư mục dự án
cd Mistake-Tracker

# 3. Chạy chương trình
python Mistake_Tracker.py
```

---

### ▶️ Hướng dẫn sử dụng

| Lựa chọn                     | Mô tả                                        |
| ---------------------------- | -------------------------------------------- |
| `1. [+] Add a New Mistake`   | Thêm lỗi mới (Môn, Lỗi, Cách sửa).           |
| `2. [*] View Mistakes`       | Xem tổng số lỗi và tỷ lệ phần trăm theo môn. |
| `3. [!] Edit/Delete Mistake` | Sửa hoặc xóa các lỗi đã ghi.                 |
| `4. [X] Exit`                | Thoát chương trình an toàn.                  |

---

### 🎨 Demo giao diện

```text
=== [ Mistake Tracker ] ===
1. [+] Add a New Mistake
2. [*] View Mistakes
3. [!] Edit/Delete Mistake
4. [X] Exit

Choose an option (1-4): 2

--- [*] View Mistakes ---
Total mistakes recorded: 15

Mistakes by Subject:
Subject         | Total mistakes | Rate      
---------------------------------------------
Math            | 10             | 66.7%
English         | 3              | 20.0%
Coding          | 2              | 13.3%

--- All Mistakes (paginated) ---
1. [Math] Wrong formula -> Correct formula (22-12-2025)
2. [Math] Calculation error -> Check steps (22-12-2025)
...
Press Enter to see more...
```

---

### 📄 Bản quyền

MIT License
Tác giả: **minx-nie**

---
=======
>>>>>>> ef2074c6f572bb8d689c90a4181b4a28ac1cb1f5
