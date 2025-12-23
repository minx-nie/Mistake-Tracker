import json
import os
import shutil
from collections import Counter
from datetime import datetime

DATA_FILE = "mistakes.json"
BACKUP_DIR = "backups"
MAX_BACKUPS = 20
DATE_FORMAT = "%Y-%m-%d"

# ================= DATA MANAGEMENT =================

def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            raw_data = json.load(f)

        valid_data = []
        for entry in raw_data:
            if not all(k in entry for k in ("subject", "mistake", "fix", "date")):
                print(f"[!] Invalid entry skipped: {entry}")
                continue

            try:
                datetime.strptime(entry["date"], DATE_FORMAT)
            except ValueError:
                print(f"[!] Invalid date skipped: {entry}")
                continue

            valid_data.append(entry)

        return valid_data

    except json.JSONDecodeError:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        corrupt = f"{DATA_FILE}.corrupt.{ts}"
        os.rename(DATA_FILE, corrupt)
        print(f"[!] Data corrupted. Renamed to {corrupt}")
        return []

    except OSError as e:
        print(f"[!] Cannot read data file: {e}")
        return []


def backup_data():
    if not os.path.exists(DATA_FILE):
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"{DATA_FILE}.{ts}.bak")

    try:
        shutil.copy2(DATA_FILE, backup_file)
    except OSError as e:
        print(f"[!] Backup failed: {e}")
        return

    try:
        backups = sorted(
            [
                os.path.join(BACKUP_DIR, f)
                for f in os.listdir(BACKUP_DIR)
                if f.startswith(DATA_FILE) and f.endswith(".bak")
            ],
            reverse=True
        )
        for old in backups[MAX_BACKUPS:]:
            os.remove(old)
    except OSError:
        pass


def save_data(data):
    backup_data()
    tmp = DATA_FILE + ".tmp"

    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, DATA_FILE)
    except OSError as e:
        print(f"[!] Save failed: {e}")

# ================= INPUT VALIDATION =================

def _contains_control_chars(s: str) -> bool:
    return any(ord(ch) < 32 or ord(ch) == 127 for ch in s)


def get_non_empty_input(prompt, max_length=300):
    while True:
        value = input(prompt).strip()

        if not value:
            print("[!] Input cannot be empty.")
            continue

        if len(value) > max_length:
            print(f"[!] Input too long (max {max_length}).")
            continue

        if _contains_control_chars(value):
            print("[!] Control characters detected.")
            continue

        return value

# ================= CORE =================

def normalize_subject(subject: str) -> str:
    return subject.strip().lower()


def add_mistake(data):
    print("\n--- [+] Add a New Mistake ---")

    subject = normalize_subject(get_non_empty_input("Subject: "))
    mistake = get_non_empty_input("Mistake: ")
    fix = get_non_empty_input("Fix: ")

    entry = {
        "subject": subject,
        "mistake": mistake,
        "fix": fix,
        "date": datetime.now().strftime(DATE_FORMAT)
    }

    data.append(entry)
    save_data(data)
    print("[OK] Mistake added.\n")


def view_mistakes(data, page_size=10):
    print("\n--- [*] View Mistakes ---")
    if not data:
        print("No mistakes recorded.\n")
        return

    keyword = input("Filter by keyword (Enter to skip): ").strip().lower()
    if keyword:
        data = [
            e for e in data
            if keyword in e["mistake"].lower()
            or keyword in e["fix"].lower()
            or keyword in e["subject"]
        ]

        if not data:
            print("No matching mistakes found.\n")
            return

    data = sorted(data, key=lambda x: x["date"], reverse=True)

    total = len(data)
    print(f"\nTotal mistakes: {total}")

    subjects = [e["subject"] for e in data]
    counter = Counter(subjects)

    print("\nMistakes by Subject:")
    print(f"{'Subject':<20} | {'Count':<5} | {'Rate'}")
    print("-" * 40)

    for sub, count in counter.most_common():
        percent = (count / total) * 100
        print(f"{sub.title()[:20]:<20} | {count:<5} | {percent:.1f}%")

    print("\n--- All Mistakes ---")
    for i in range(0, total, page_size):
        for idx, e in enumerate(data[i:i+page_size], start=i+1):
            print(
                f"{idx}. [{e['subject'].title()}] "
                f"{e['mistake']} -> {e['fix']} ({e['date']})"
            )
        if i + page_size < total:
            input("Press Enter to continue...")


def edit_or_delete_mistake(data):
    if not data:
        print("No mistakes recorded.\n")
        return

    print("\n--- [*] Edit/Delete ---")
    for i, e in enumerate(data, start=1):
        print(f"{i}. [{e['subject'].title()}] {e['mistake']}")

    choice = input("Choose number (0 = cancel): ").strip()
    if not choice.isdigit():
        return

    idx = int(choice)
    if idx == 0 or idx > len(data):
        return

    entry = data[idx - 1]
    action = input("(e)dit / (d)elete: ").strip().lower()

    if action == "d":
        confirm = input("Confirm delete? (yes/no): ").lower()
        if confirm == "yes":
            data.pop(idx - 1)
            save_data(data)
            print("[OK] Deleted.")

    elif action == "e":
        print("Leave blank to keep current value.")

        subject = input(f"Subject [{entry['subject']}]: ").strip()
        if subject:
            subject = normalize_subject(get_non_empty_input("Re-enter subject: "))

        mistake = input(f"Mistake [{entry['mistake']}]: ").strip()
        if mistake:
            mistake = get_non_empty_input("Re-enter mistake: ")

        fix = input(f"Fix [{entry['fix']}]: ").strip()
        if fix:
            fix = get_non_empty_input("Re-enter fix: ")

        entry["subject"] = subject or entry["subject"]
        entry["mistake"] = mistake or entry["mistake"]
        entry["fix"] = fix or entry["fix"]

        save_data(data)
        print("[OK] Updated.")

# ================= MAIN =================

def main():
    data = load_data()

    while True:
        print("\n=== Mistake Tracker ===")
        print("1. Add")
        print("2. View")
        print("3. Edit/Delete")
        print("4. Exit")

        c = input("Choose (1-4): ").strip()
        if c == "1":
            add_mistake(data)
        elif c == "2":
            view_mistakes(data)
        elif c == "3":
            edit_or_delete_mistake(data)
        elif c == "4":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
