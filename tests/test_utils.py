"""Test utilities module."""

import logging

from src.utils import format_output, setup_logging, validate_config


def test_format_output():
    """Test output formatting."""
    data = {"key": "value", "number": 42}
    result = format_output(data)

    assert isinstance(result, str)
    assert "key" in result
    assert "value" in result


def test_validate_config_valid():
    """Test validation with valid config."""
    config = {
        "app": {"name": "test"},
        "logging": {"level": "INFO"},
        "output": {"dir": "outputs"},
    }

    assert validate_config(config) is True


def test_validate_config_invalid():
    """Test validation with invalid config."""
    config = {
        "app": {"name": "test"}
        # Missing "logging" and "output"
    }

    assert validate_config(config) is False


def test_setup_logging(caplog):
    """Test the setup_logging function."""
    with caplog.at_level(logging.INFO):
        setup_logging("INFO")
    assert "Logging configured at INFO level" in caplog.text
