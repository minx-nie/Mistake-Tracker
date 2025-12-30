import json
import os
import shutil
import uuid
from datetime import datetime

DATA_FILE = "mistakes.json"
BACKUP_DIR = "backups"
MAX_BACKUPS = 20
DATE_FORMAT = "%Y-%m-%d"

# ================= UTILITIES =================


def input_clean(prompt: str, required: bool = True) -> str:
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("[!] Input cannot be empty.")


def normalize_subject(subject: str) -> str:
    return subject.strip().lower()


# ================= DATA MANAGEMENT =================


def backup_data():
    if not os.path.exists(DATA_FILE):
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"{DATA_FILE}.{timestamp}.bak")

    try:
        shutil.copy2(DATA_FILE, backup_file)

        backups = sorted(
            (os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR) if f.endswith(".bak")),
            reverse=True,
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
        with open(DATA_FILE, encoding="utf-8") as f:
            data = json.load(f)

        valid_data = []
        modified = False

        for entry in data:
            if not all(k in entry for k in ("subject", "mistake", "fix", "date")):
                continue

            if "id" not in entry:
                entry["id"] = str(uuid.uuid4())[:8]
                modified = True

            valid_data.append(entry)

        if modified:
            save_data(valid_data)

        return valid_data

    except json.JSONDecodeError:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        corrupt = f"{DATA_FILE}.corrupt.{ts}"
        os.rename(DATA_FILE, corrupt)
        print(f"[!] Data corrupted. Renamed to {corrupt}")
        return []

    except OSError:
        return []


# ================= FEATURES =================


def add_mistake(data):
    print("\n--- [+] Add a New Mistake ---")

    subject = normalize_subject(input_clean("Subject: "))
    mistake = input_clean("Mistake Description: ")
    fix = input_clean("Fix/Correction: ")

    new_entry = {
        "id": str(uuid.uuid4())[:8],
        "subject": subject,
        "mistake": mistake,
        "fix": fix,
        "date": datetime.now().strftime(DATE_FORMAT),
    }

    data.append(new_entry)
    if save_data(data):
        print(f"[OK] Mistake added! (ID: {new_entry['id']})")


def view_mistakes(data):
    print("\n--- [*] View Mistakes ---")

    if not data:
        print("No mistakes recorded.")
        return

    print("1. View All")
    print("2. Search")
    choice = input("Choice: ").strip()

    results = data
    if choice == "2":
        keyword = input("Keyword: ").strip().lower()
        results = [x for x in data if keyword in x["subject"] or keyword in x["mistake"]]

    for entry in sorted(results, key=lambda x: x["date"], reverse=True):
        print(f"{entry['id']} | {entry['date']} | [{entry['subject']}] {entry['mistake']}")


def edit_or_delete_mistake(data):
    if not data:
        print("No data available.")
        return

    target_id = input("Enter ID: ").strip()

    for _i, entry in enumerate(data):
        if entry["id"] == target_id:
            break
    else:
        print("[!] ID not found.")
        return

    i = _i

    action = input("Edit (e) / Delete (d): ").lower()

    if action == "d":
        if input("Confirm delete? (y/n): ").lower() == "y":
            data.pop(i)
            save_data(data)
            print("[OK] Deleted.")
        return

    if action == "e":
        new_sub = input_clean(f"Subject [{entry['subject']}]: ", False)
        new_mis = input_clean(f"Mistake [{entry['mistake']}]: ", False)
        new_fix = input_clean(f"Fix [{entry['fix']}]: ", False)

        if new_sub:
            entry["subject"] = normalize_subject(new_sub)
        if new_mis:
            entry["mistake"] = new_mis
        if new_fix:
            entry["fix"] = new_fix

        save_data(data)
        print("[OK] Updated.")


# ================= MAIN =================


def main():
    data = load_data()

    while True:
        print("\n=== Mistake Tracker V2 ===")
        print(f"Total records: {len(data)}")
        print("1. Add")
        print("2. View/Search")
        print("3. Edit/Delete")
        print("4. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_mistake(data)
        elif choice == "2":
            view_mistakes(data)
        elif choice == "3":
            edit_or_delete_mistake(data)
        elif choice == "4":
            break
        else:
            print("[!] Invalid choice.")


if __name__ == "__main__":
    main()
