import json
import os
import shutil
from datetime import datetime
from collections import Counter

DATA_FILE = 'mistakes.json'

# ================= DATA MANAGEMENT ================

def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[!] Data file is corrupted (invalid JSON).")
        return []
    except OSError as e:
        print(f"[!] Cannot read data file: {e}")
        return []

def backup_data():
    if os.path.exists(DATA_FILE):
        backup_file = DATA_FILE + ".bak"
        try:
            shutil.copy2(DATA_FILE, backup_file)
            print(f"[!] Backup created at {backup_file}")
        except OSError as e:
            print(f"[!] Failed to create backup: {e}")

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

def get_non_empty_input(prompt, max_length=200):
    while True:
        value = input(prompt).strip()
        if not value:
            print("[!] Input cannot be empty. Please try again.")
        elif len(value) > max_length:
            print(f"[!] Input too long (max {max_length} characters).")
        else:
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
    print("-" *40)
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
        subject = input(f"Subject [{entry['subject']}]: ").strip() or entry['subject']
        mistake = input(f"Mistake [{entry['mistake']}]: ").strip() or entry['mistake']
        fix = input(f"Fix [{entry['fix']}]: ").strip() or entry['fix']
        entry.update({"subject": subject, "mistake": mistake, "fix": fix})
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
