# 📉 Mistake Tracker

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Tests](https://img.shields.io/github/actions/workflow/status/minx-nie/Mistake-Tracker/ci.yml?branch=main&label=Tests&style=for-the-badge&logo=github)](https://github.com/minx-nie/Mistake-Tracker/actions)

**🎯 Track your learning mistakes. Identify weak points. Improve efficiently.**

</div>

---

## 📖 Mục lục

- [Giới thiệu](#-giới-thiệu)
- [Cài đặt](#-cài-đặt)
- [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [Đóng góp](#-đóng-góp)

---

## 📌 Giới thiệu

**Mistake Tracker** là công cụ dòng lệnh (CLI) giúp học sinh, sinh viên ghi lại và theo dõi các lỗi sai trong quá trình học tập.

### ✨ Tính năng chính

| Tính năng | Mô tả |
|-----------|-------|
| ✍️ **Ghi lỗi** | Nhập môn học, mô tả lỗi và cách khắc phục |
| 📊 **Thống kê** | Xem tỷ lệ % lỗi theo từng môn học |
| 🔍 **Tìm kiếm** | Lọc lỗi theo từ khóa |
| ✏️ **Sửa/Xóa** | Chỉnh sửa hoặc xóa các lỗi đã ghi |
| 💾 **Auto-backup** | Tự động sao lưu dữ liệu (20 bản gần nhất) |

---

## 🚀 Cài đặt

### Cách 1: Chạy trực tiếp

```bash
# Clone repo
git clone https://github.com/minx-nie/Mistake-Tracker.git
cd Mistake-Tracker

# Chạy
python -m mistake_tracker
```

### Cách 2: Cài đặt như package

```bash
# Cài đặt
pip install -e .

# Chạy từ bất kỳ đâu
mistake-tracker
```

---

## 📖 Hướng dẫn sử dụng

### Menu chính

Khi chạy chương trình, bạn sẽ thấy menu:

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

### 1️⃣ Thêm lỗi mới

Chọn `1` → Nhập thông tin:

```
━━━ ➕ Add New Mistake ━━━
Subject: math
Mistake: Nhầm công thức tính diện tích
Fix: S = pi * r^2 không phải 2*pi*r

✅ Mistake added successfully!
```

---

### 2️⃣ Xem danh sách lỗi

Chọn `2` → Xem thống kê và danh sách:

```
━━━ 📋 View Mistakes ━━━
🔍 Filter by keyword (Enter to skip):

📊 Statistics (Total: 15)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subject              │ Count │  Rate
─────────────────────┼───────┼───────
Math                 │    10 │ 66.7%
English              │     3 │ 20.0%
Coding               │     2 │ 13.3%

📝 All Mistakes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Math] Nhầm công thức → S = pi*r^2 (2024-12-23)
2. [Math] Sai dấu → Kiểm tra lại các bước (2024-12-22)
...
```

**Lọc theo từ khóa:** Nhập từ khóa để tìm lỗi cụ thể.

---

### 3️⃣ Sửa/Xóa lỗi

Chọn `3` → Chọn số thứ tự → `e` để sửa hoặc `d` để xóa:

```
━━━ ✏️ Edit/Delete ━━━
1. [Math] Nhầm công thức
2. [English] Sai ngữ pháp

Choose number (0 = cancel): 1
(e)dit / (d)elete: e

💡 Leave blank to keep current value.
Subject [math]:
Mistake [Nhầm công thức]: Nhầm công thức tính thể tích
Fix [S = pi*r^2]: V = 4/3 * pi * r^3

✅ Updated.
```

---

### 4️⃣ Thoát

Chọn `4` để thoát chương trình an toàn.

---

## 📂 Cấu trúc dự án

```
Mistake-Tracker/
├── src/mistake_tracker/    # Source code
│   ├── __init__.py
│   ├── __main__.py         # Entry point
│   ├── cli.py              # Giao diện CLI
│   └── data.py             # Quản lý dữ liệu
├── tests/                  # Unit tests
├── .github/workflows/      # CI/CD
├── pyproject.toml          # Cấu hình dự án
└── README.md
```

---

## 🤝 Đóng góp

Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết cách đóng góp.

---

## 📄 License

MIT License - Xem [LICENSE](LICENSE) để biết thêm chi tiết.

---

<div align="center">

**Made with ❤️ by [Minx-nie](https://github.com/minx-nie)**

</div>