import json
import os
from datetime import datetime
from collections import Counter

DATA_FILE = 'mistakes.json'

# ================= CONSTANTS =================

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []
    
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii= False ,indent=4)
    

# ================ DATA MANAGEMENT ================

def add_mistake(data):
    print("\n--- ✍️  Add a New Mistake ---")
    subject = input("Subject: ").strip()
    mistake = input("Mistake Description: ").strip()
    fix = input("Fix/Correction: ").strip()

    today = datetime.now().strftime("%d-%m-%Y")

    new_entry = {
        "subject": subject,
        "mistake": mistake,
        "fix": fix,
        "date": today
    }

    data.append(new_entry)
    save_data(data)
    print("✅ Mistake added successfully!\n")


def view_mistakes(data):
    print("\n--- 📚 View Mistakes ---")
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


# ================= MAIN MENU =================

def main():
    data = load_data()

    while True:
        print("\n=== Mistake Tracker ===")
        print("1. Add a New Mistake")
        print("2. View Mistakes")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            add_mistake(data)
        elif choice == '2':
            view_mistakes(data)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
