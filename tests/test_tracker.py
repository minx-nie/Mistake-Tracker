"""Unit tests for Mistake Tracker."""

import json
import os
import tempfile
from pathlib import Path

import pytest

from mistake_tracker.data import (
    add_mistake,
    get_statistics,
    load_data,
    save_data,
)


@pytest.fixture
def temp_data_file(tmp_path: Path) -> str:
    """Create a temporary data file path."""
    return str(tmp_path / "test_mistakes.json")


@pytest.fixture
def sample_data() -> list[dict]:
    """Sample mistake data for testing."""
    return [
        {"subject": "math", "mistake": "Wrong formula", "fix": "Check formula", "date": "2024-01-15"},
        {"subject": "math", "mistake": "Calculation error", "fix": "Double check", "date": "2024-01-16"},
        {"subject": "english", "mistake": "Grammar issue", "fix": "Review rules", "date": "2024-01-17"},
    ]


class TestLoadData:
    """Tests for load_data function."""

    def test_load_empty_file(self, temp_data_file: str) -> None:
        """Load returns empty list when file doesn't exist."""
        data = load_data(temp_data_file)
        assert data == []

    def test_load_valid_data(self, temp_data_file: str, sample_data: list) -> None:
        """Load returns valid entries from file."""
        with open(temp_data_file, "w") as f:
            json.dump(sample_data, f)

        data = load_data(temp_data_file)
        assert len(data) == 3
        assert data[0]["subject"] == "math"

    def test_load_skips_invalid_entries(self, temp_data_file: str) -> None:
        """Load skips entries missing required fields."""
        invalid_data = [
            {"subject": "math"},  # Missing fields
            {"subject": "english", "mistake": "Test", "fix": "Fix", "date": "2024-01-01"},
        ]
        with open(temp_data_file, "w") as f:
            json.dump(invalid_data, f)

        data = load_data(temp_data_file)
        assert len(data) == 1


class TestSaveData:
    """Tests for save_data function."""

    def test_save_creates_file(self, temp_data_file: str, sample_data: list) -> None:
        """Save creates the data file."""
        result = save_data(sample_data, temp_data_file)
        
        assert result is True
        assert os.path.exists(temp_data_file)

    def test_save_and_load_roundtrip(self, temp_data_file: str, sample_data: list) -> None:
        """Data can be saved and loaded back."""
        save_data(sample_data, temp_data_file)
        loaded = load_data(temp_data_file)

        assert len(loaded) == len(sample_data)
        assert loaded[0]["subject"] == sample_data[0]["subject"]


class TestAddMistake:
    """Tests for add_mistake function."""

    def test_add_creates_entry(self) -> None:
        """Adding a mistake creates proper entry."""
        data: list = []
        entry = add_mistake(data, "Math", "Wrong answer", "Check work")

        assert len(data) == 1
        assert entry["subject"] == "math"  # Normalized to lowercase
        assert entry["mistake"] == "Wrong answer"
        assert "date" in entry


class TestGetStatistics:
    """Tests for get_statistics function."""

    def test_empty_data_returns_empty(self) -> None:
        """Empty data returns empty statistics."""
        stats = get_statistics([])
        assert stats == {}

    def test_calculates_percentages(self, sample_data: list) -> None:
        """Calculates correct percentages by subject."""
        stats = get_statistics(sample_data)

        assert "math" in stats
        assert stats["math"][0] == 2  # Count
        assert abs(stats["math"][1] - 66.67) < 1  # Percentage

        assert "english" in stats
        assert stats["english"][0] == 1
        assert abs(stats["english"][1] - 33.33) < 1
