# 📉 Mistake Tracker

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python 3.x">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License MIT">
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen" alt="Status Stable">
  <img src="https://img.shields.io/badge/Type-Education%20Tool-orange" alt="Education Tool">
</div>

---

<div align="center">
🇬🇧 [English](#english) | 🇻🇳 [Tiếng Việt](#vietnamese)
</div>

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