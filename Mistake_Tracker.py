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

def normalize_subject(subject: str) -> str:
    return subject.strip().lower()

def backup_data():
    if not os.path.exists(DATA_FILE):
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"{DATA_FILE}.{timestamp}.bak")

    try:
        shutil.copy2(DATA_FILE, backup_file)
        
        backups = sorted(
            [os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR) if f.endswith(".bak")],
            reverse=True
        )
        for old in backups[MAX_BACKUPS:]:
            os.remove(old)
    except OSError:
        pass

def save_data(data):
    backup_data()
    tmp_file = DATA_FILE + ".tmp"

    try:
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_file, DATA_FILE)
        return True
    except OSError:
        if os.path.exists(tmp_file):
            os.remove(tmp_file)
        print("[!] Failed to save data.")
        return False

def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        valid_data = []
        is_modified = False

        for entry in data:
            if not all(key in entry for key in ("subject", "mistake", "fix", "date")):
                continue

            if "id" not in entry:
                entry["id"] = str(uuid.uuid4())[:8]
                is_modified = True
            
            valid_data.append(entry)

        if is_modified:
            save_data(valid_data)

        return valid_data

    except json.JSONDecodeError:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        corrupt_file = f"{DATA_FILE}.corrupt.{timestamp}"
        if os.path.exists(DATA_FILE):
            os.rename(DATA_FILE, corrupt_file)
        print(f"[!] Data corrupted. Renamed to {corrupt_file}")
        return []
    except OSError:
        return []

def add_mistake(data):
    print("\n--- [+] Add a New Mistake ---")

    subject = normalize_subject(input_clean("Subject: "))
    mistake = input_clean("Mistake Description: ")
    fix = input_clean("Fix/Correction: ")
    today = datetime.now().strftime(DATE_FORMAT)
    new_id = str(uuid.uuid4())[:8]

    new_entry = {
        "id": new_id,
        "subject": subject,
        "mistake": mistake,
        "fix": fix,
        "date": today
    }

    data.append(new_entry)
    if save_data(data):
        print(f"[OK] Mistake added successfully! (ID: {new_id})")

def view_mistakes(data):
    print("\n--- [*] View Mistakes ---")
    if not data:
        print("No mistakes recorded yet.\n")
        return

    print("1. View All")
    print("2. Search")
    choice = input("Choice: ").strip()

    results = data
    if choice == "2":
        keyword = input("Enter keyword: ").strip().lower()
        results = [x for x in data if keyword in x["subject"] or keyword in x["mistake"]]

    results = sorted(results, key=lambda x: x["date"], reverse=True)

    print(f"\nFound: {len(results)} entries")
    for entry in results:
        print(f"ID: {entry['id']} | {entry['date']} | [{entry['subject']}] {entry['mistake']}")

def edit_or_delete_mistake(data):
    if not data:
        print("No mistakes recorded yet.\n")
        return

    print("\n--- [*] Edit/Delete Mistakes ---")
    target_id = input("Enter ID to Edit/Delete: ").strip()
    
    found_index = -1
    for i, entry in enumerate(data):
        if entry["id"] == target_id:
            found_index = i
            break
    
    if found_index == -1:
        print("[!] ID not found.")
        return

    entry = data[found_index]
    print(f"Selected: [{entry['subject']}] {entry['mistake']}")
    action = input("Enter 'e' to edit, 'd' to delete: ").strip().lower()

    if action == "d":
        confirm = input("Confirm delete? (y/n): ").strip().lower()
        if confirm == "y":
            data.pop(found_index)
            save_data(data)
            print("[OK] Mistake deleted.")

    elif action == "e":
        print("Leave blank to keep current value.")

        new_sub = input_clean(f"Subject [{entry['subject']}]: ", required=False)
        if new_sub:
            entry["subject"] = normalize_subject(new_sub)

        new_mis = input_clean(f"Mistake [{entry['mistake']}]: ", required=False)
        if new_mis:
            entry["mistake"] = new_mis

        new_fix = input_clean(f"Fix [{entry['fix']}]: ", required=False)
        if new_fix:
            entry["fix"] = new_fix

        save_data(data)
        print("[OK] Mistake updated.")

def main():
    if os.path.exists(DATA_FILE + ".tmp"):
        try:
            os.remove(DATA_FILE + ".tmp")
        except OSError:
            pass

    data = load_data()

    while True:
        print("\n=== Mistake Tracker V2 ===")
        print(f"Total: {len(data)} records")
        print("1. Add a New Mistake")
        print("2. View / Search Mistakes")
        print("3. Edit/Delete Mistake (by ID)")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_mistake(data)
        elif choice == "2":
            view_mistakes(data)
        elif choice == "3":
            edit_or_delete_mistake(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()