"""CLI interface for Mistake Tracker."""

from __future__ import annotations

from collections import Counter

from mistake_tracker.data import (
    MistakeEntry,
    add_mistake,
    get_statistics,
    load_data,
    save_data,
)


def print_header() -> None:
    """Print the main menu header."""
    print("\n╔══════════════════════════════════════╗")
    print("║       📉 MISTAKE TRACKER             ║")
    print("╠══════════════════════════════════════╣")
    print("║  [1] ➕ Add New Mistake              ║")
    print("║  [2] 📋 View Mistakes                ║")
    print("║  [3] ✏️  Edit/Delete                  ║")
    print("║  [4] 🚪 Exit                         ║")
    print("╚══════════════════════════════════════╝")


def get_input(prompt: str, max_length: int = 300) -> str:
    """Get validated user input.

    Args:
        prompt: Input prompt to display.
        max_length: Maximum input length.

    Returns:
        Validated input string.
    """
    while True:
        value = input(prompt).strip()

        if not value:
            print("⚠️  Input cannot be empty.")
            continue

        if len(value) > max_length:
            print(f"⚠️  Input too long (max {max_length}).")
            continue

        # Check for control characters
        if any(ord(ch) < 32 or ord(ch) == 127 for ch in value):
            print("⚠️  Invalid characters detected.")
            continue

        return value


def cmd_add(data: list[MistakeEntry]) -> None:
    """Add a new mistake."""
    print("\n━━━ ➕ Add New Mistake ━━━")

    subject = get_input("Subject: ")
    mistake = get_input("Mistake: ")
    fix = get_input("Fix: ")

    add_mistake(data, subject, mistake, fix)
    save_data(data)

    print("✅ Mistake added successfully!\n")


def cmd_view(data: list[MistakeEntry], page_size: int = 10) -> None:
    """View all mistakes with statistics."""
    print("\n━━━ 📋 View Mistakes ━━━")

    if not data:
        print("📭 No mistakes recorded yet.\n")
        return

    # Filter option
    keyword = input("🔍 Filter by keyword (Enter to skip): ").strip().lower()
    if keyword:
        data = [
            e for e in data
            if keyword in e["mistake"].lower()
            or keyword in e["fix"].lower()
            or keyword in e["subject"]
        ]

        if not data:
            print("❌ No matching mistakes found.\n")
            return

    # Sort by date (newest first)
    data = sorted(data, key=lambda x: x["date"], reverse=True)

    # Statistics
    total = len(data)
    stats = get_statistics(data)

    print(f"\n📊 Statistics (Total: {total})")
    print("━" * 40)
    print(f"{'Subject':<20} │ {'Count':>5} │ {'Rate':>6}")
    print("─" * 40)

    for subject, (count, rate) in stats.items():
        print(f"{subject.title()[:20]:<20} │ {count:>5} │ {rate:>5.1f}%")

    # List all mistakes with pagination
    print(f"\n📝 All Mistakes")
    print("━" * 50)

    for i in range(0, total, page_size):
        for idx, e in enumerate(data[i:i + page_size], start=i + 1):
            print(
                f"{idx}. [{e['subject'].title()}] "
                f"{e['mistake']} → {e['fix']} ({e['date']})"
            )
        if i + page_size < total:
            input("\n⏩ Press Enter for more...")


def cmd_edit_delete(data: list[MistakeEntry]) -> None:
    """Edit or delete a mistake."""
    if not data:
        print("📭 No mistakes recorded.\n")
        return

    print("\n━━━ ✏️ Edit/Delete ━━━")

    for i, e in enumerate(data, start=1):
        print(f"{i}. [{e['subject'].title()}] {e['mistake']}")

    choice = input("\nChoose number (0 = cancel): ").strip()
    if not choice.isdigit():
        return

    idx = int(choice)
    if idx == 0 or idx > len(data):
        return

    entry = data[idx - 1]
    action = input("(e)dit / (d)elete: ").strip().lower()

    if action == "d":
        confirm = input("⚠️  Confirm delete? (yes/no): ").lower()
        if confirm == "yes":
            data.pop(idx - 1)
            save_data(data)
            print("✅ Deleted.\n")

    elif action == "e":
        print("💡 Leave blank to keep current value.\n")

        new_subject = input(f"Subject [{entry['subject']}]: ").strip()
        new_mistake = input(f"Mistake [{entry['mistake']}]: ").strip()
        new_fix = input(f"Fix [{entry['fix']}]: ").strip()

        if new_subject:
            entry["subject"] = new_subject.lower()
        if new_mistake:
            entry["mistake"] = new_mistake
        if new_fix:
            entry["fix"] = new_fix

        save_data(data)
        print("✅ Updated.\n")


def main() -> None:
    """Main entry point."""
    data = load_data()

    while True:
        print_header()

        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            cmd_add(data)
        elif choice == "2":
            cmd_view(data)
        elif choice == "3":
            cmd_edit_delete(data)
        elif choice == "4":
            print("\n👋 Goodbye!\n")
            break
        else:
            print("⚠️  Invalid choice.\n")


if __name__ == "__main__":
    main()
