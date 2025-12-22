import json
import os
import shutil
from datetime import datetime
from collections import Counter

DATA_FILE = 'mistakes.json'
BACKUP_DIR = 'backups'
MAX_BACKUPS = 20

# ================= DATA MANAGEMENT ================

def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        valid_data = []
        for entry in raw_data:
            if all(key in entry for key in ("subject", "mistake", "fix", "date")):
                valid_data.append(entry)
            else:
                print(f"[!] Invalid entry skipped: {entry}")
        return valid_data
    except json.JSONDecodeError:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        corrupt_file = f"{DATA_FILE}.corrupted.{timestamp}"
        os.rename(DATA_FILE, corrupt_file)
        print(f"[!] Data file is corrupted. Renamed to {corrupt_file}")
        return []
    except OSError as e:
        print(f"[!] Cannot read data file: {e}")
        return []

def backup_data():
    if os.path.exists(DATA_FILE):
        return
    os.makedirs(BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"{DATA_FILE}.{timestamp}.bak")
    try:
        shutil.copy2(DATA_FILE, backup_file)
    except OSError as e:
        print(f"[!] Failed to create backup: {e}")
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

        for old_backup in backups[MAX_BACKUPS:]:
            os.remove(old_backup)
    except OSError as e:
        pass
    
def save_data(data):
    backup_data()
    tmp_file = DATA_FILE + ".tmp"
    try:
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        os.replace(tmp_file, DATA_FILE)
    except OSError as e:
        print(f"[!] Failed to save data: {e}")

# ================= INPUT VALIDATION =================

def _contains_control_chars(s: str) -> bool:
    for ch in s:
        code = ord(ch)
        if code < 32 or code == 127:
            return True
    return False

def get_non_empty_input(prompt, max_length=200):
    while True:
        value = input(prompt).strip()

        if not value:
            print("[!] Input cannot be empty. Please try again.")
            continue

        if len(value) > max_length:
            print(f"[!] Input too long (max {max_length} characters).")
            continue

        if _contains_control_chars(value):
            print("[!] Invalid control characters detected. Please remove them and try again.")
            continue

        return value

# ================= CORE FUNCTIONS =================

def add_mistake(data):
    print("\n--- [+]  Add a New Mistake ---")
    subject = get_non_empty_input("Subject: ")
    mistake = get_non_empty_input("Mistake Description: ")
    fix = get_non_empty_input("Fix/Correction: ")

    today = datetime.now().strftime("%d-%m-%Y")

    new_entry = {
        "subject": subject,
        "mistake": mistake,
        "fix": fix,
        "date": today
    }

    data.append(new_entry)
    save_data(data)
    print("[!] Mistake added successfully!\n")

def view_mistakes(data, page_size=10):
    print("\n--- [*] View Mistakes ---")
    if not data:
        print("No mistakes recorded yet.\n")
        return

    total_errors = len(data)
    print(f"Total mistakes recorded: {total_errors}")

    subjects = [item['subject'] for item in data]
    counter = Counter(subjects)

    print("\nMistakes by Subject:")
    print(f"{'Subject':<15} | {'Total mistakes':<10} | {'Rate':<10}")
    print("-" * 40)
    for sub, count in counter.most_common():
        percent = (count / total_errors) * 100
        print(f"{sub:<15} | {count:<10} | {percent:.1f}%")

    print("\n--- All Mistakes (paginated) ---")
    start = 0
    while start < total_errors:
        end = min(start + page_size, total_errors)
        for i in range(start, end):
            entry = data[i]
            print(f"{i+1}. [{entry['subject']}] {entry['mistake']} -> {entry['fix']} ({entry['date']})")
        start = end
        if start < total_errors:
            input("Press Enter to see more...")

def edit_or_delete_mistake(data):
    if not data:
        print("No mistakes recorded yet.\n")
        return

    print("\n--- [*] Edit/Delete Mistakes ---")
    for i, entry in enumerate(data, start=1):
        print(f"{i}. [{entry['subject']}] {entry['mistake']} -> {entry['fix']} ({entry['date']})")

    choice = input("Enter the number to edit/delete (or 0 to cancel): ").strip()
    if not choice.isdigit():
        print("[!] Invalid input.")
        return
    choice = int(choice)
    if choice == 0:
        return
    if choice < 1 or choice > len(data):
        print("[!] Choice out of range.")
        return

    entry = data[choice - 1]
    action = input("Enter 'e' to edit, 'd' to delete, or anything else to cancel: ").strip().lower()
    if action == 'd':
        confirm = input(f"Are you sure you want to delete '{entry['mistake']}'? (y/n): ").strip().lower()
        if confirm == 'y':
            data.pop(choice - 1)
            save_data(data)
            print("[!] Mistake deleted.")
    elif action == 'e':
        print("Leave blank to keep current value.")
        subject = input(f"Subject [{entry['subject']}]: ").strip()
        if subject:
            subject = get_non_empty_input("Re-enter Subject: ")  

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
        print("[!] Mistake updated.")
    else:
        print("Cancelled.")

# ================= MAIN MENU =================

def main():
    data = load_data()

    while True:
        print("\n=== Mistake Tracker ===")
        print("1. Add a New Mistake")
        print("2. View Mistakes")
        print("3. Edit/Delete Mistake")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_mistake(data)
        elif choice == '2':
            view_mistakes(data)
        elif choice == '3':
            edit_or_delete_mistake(data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
