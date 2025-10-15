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
    required_keys = ["app", "logging", "output"]
    
    for key in required_keys:
        if key not in config:
            log.error(f"Missing required configuration key: {key}")
            return False
    
    log.debug("Configuration validation passed")
    return True


def setup_logging(level: str = "INFO") -> None:
    """
    Configure logging for the application.

    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    log.info(f"Logging configured at {level} level")
