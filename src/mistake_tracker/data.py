"""Data management module for Mistake Tracker."""

from __future__ import annotations

import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import TypedDict


class MistakeEntry(TypedDict):
    """Type definition for a mistake entry."""

    subject: str
    mistake: str
    fix: str
    date: str


DATA_FILE = "mistakes.json"
BACKUP_DIR = "backups"
MAX_BACKUPS = 20
DATE_FORMAT = "%Y-%m-%d"


def load_data(data_file: str = DATA_FILE) -> list[MistakeEntry]:
    """Load mistake data from JSON file.

    Args:
        data_file: Path to the data file.

    Returns:
        List of mistake entries.
    """
    if not os.path.exists(data_file):
        return []

    try:
        with open(data_file, encoding="utf-8") as f:
            raw_data = json.load(f)

        valid_data: list[MistakeEntry] = []
        for entry in raw_data:
            if not all(k in entry for k in ("subject", "mistake", "fix", "date")):
                continue

            try:
                datetime.strptime(entry["date"], DATE_FORMAT)
            except ValueError:
                continue

            valid_data.append(entry)

        return valid_data

    except json.JSONDecodeError:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        corrupt = f"{data_file}.corrupt.{ts}"
        os.rename(data_file, corrupt)
        return []

    except OSError:
        return []


def backup_data(data_file: str = DATA_FILE) -> None:
    """Create a backup of the data file.

    Args:
        data_file: Path to the data file.
    """
    if not os.path.exists(data_file):
        return

    Path(BACKUP_DIR).mkdir(exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = Path(BACKUP_DIR) / f"{data_file}.{ts}.bak"

    try:
        shutil.copy2(data_file, backup_file)
    except OSError:
        return

    # Rotate old backups
    try:
        backups = sorted(
            Path(BACKUP_DIR).glob(f"{data_file}.*.bak"),
            reverse=True,
        )
        for old in backups[MAX_BACKUPS:]:
            old.unlink()
    except OSError:
        pass


def save_data(data: list[MistakeEntry], data_file: str = DATA_FILE) -> bool:
    """Save mistake data to JSON file.

    Args:
        data: List of mistake entries.
        data_file: Path to the data file.

    Returns:
        True if save was successful.
    """
    backup_data(data_file)
    tmp = data_file + ".tmp"

    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, data_file)
        return True
    except OSError:
        return False


def add_mistake(
    data: list[MistakeEntry],
    subject: str,
    mistake: str,
    fix: str,
) -> MistakeEntry:
    """Add a new mistake entry.

    Args:
        data: List of existing mistakes.
        subject: Subject name.
        mistake: Mistake description.
        fix: How to fix the mistake.

    Returns:
        The newly created entry.
    """
    entry: MistakeEntry = {
        "subject": subject.strip().lower(),
        "mistake": mistake.strip(),
        "fix": fix.strip(),
        "date": datetime.now().strftime(DATE_FORMAT),
    }
    data.append(entry)
    return entry


def get_statistics(data: list[MistakeEntry]) -> dict[str, tuple[int, float]]:
    """Calculate statistics by subject.

    Args:
        data: List of mistake entries.

    Returns:
        Dict mapping subject to (count, percentage).
    """
    if not data:
        return {}

    total = len(data)
    counts: dict[str, int] = {}

    for entry in data:
        subject = entry["subject"]
        counts[subject] = counts.get(subject, 0) + 1

    return {
        subject: (count, (count / total) * 100)
        for subject, count in sorted(counts.items(), key=lambda x: -x[1])
    }
