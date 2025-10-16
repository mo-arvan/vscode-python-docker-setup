"""
Utility functions for the application.

This module demonstrates how to organize helper functions in a separate module.
"""

import logging
from typing import Any

log = logging.getLogger(__name__)


def format_output(data: dict[str, Any], indent: int = 2) -> str:
    """
    Format dictionary output for display.

    Args:
        data: Dictionary to format
        indent: Number of spaces for indentation

    Returns:
        Formatted string representation
    """
    import json
    return json.dumps(data, indent=indent)


def validate_config(config: dict[str, Any]) -> bool:
    """
    Validate configuration dictionary.

    Args:
        config: Configuration dictionary to validate

    Returns:
        True if valid, False otherwise
    """
    required_keys = ["app", "logging"]
    
    for key in required_keys:
        if key not in config:
            log.error(f"Missing required configuration key: {key}")
            return False
    
    log.debug("Configuration validation passed")
    return True
