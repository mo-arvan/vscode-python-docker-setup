"""Test utilities module."""

from src.utils import format_output, validate_config


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
    }

    assert validate_config(config) is True


def test_validate_config_invalid():
    """Test validation with invalid config."""
    config = {
        "app": {"name": "test"}
        # Missing "logging"
    }

    assert validate_config(config) is False
