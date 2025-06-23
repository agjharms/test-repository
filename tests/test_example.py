"""
Test module for test-package.
This module contains a simple test that always passes.
"""

import pytest


def test_always_passes():
    """A simple test that always passes."""
    assert True


def test_basic_math():
    """Another simple test demonstrating basic assertions."""
    assert 1 + 1 == 2
    assert 2 * 3 == 6


class TestExample:
    """Example test class."""

    def test_string_operations(self):
        """Test basic string operations."""
        text = "hello world"
        assert text.upper() == "HELLO WORLD"
        assert len(text) == 11

    def test_list_operations(self):
        """Test basic list operations."""
        numbers = [1, 2, 3, 4, 5]
        assert len(numbers) == 5
        assert sum(numbers) == 15
        assert max(numbers) == 5


if __name__ == "__main__":
    pytest.main([__file__])