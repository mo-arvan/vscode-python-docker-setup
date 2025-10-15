"""Test module for main application."""

import logging
import pytest
from omegaconf import OmegaConf

from src.main import run_app


def test_example():
    """Example test case."""
    assert True


def test_config_loading():
    """Test that configuration can be loaded."""
    config = OmegaConf.create({
        "app": {
            "name": "test-app",
            "version": "0.1.0",
            "environment": "test"
        },
        "output": {
            "dir": "test_outputs",
            "save_results": False
        }
    })

    assert config.app.name == "test-app"
    assert config.output.save_results is False


def test_output_directory_creation(tmp_path):
    """Test that output directory can be created."""
    test_dir = tmp_path / "outputs"
    test_dir.mkdir(parents=True, exist_ok=True)

    assert test_dir.exists()
    assert test_dir.is_dir()


def test_run_app(sample_config, caplog):
    """Test the core application logic."""
    with caplog.at_level(logging.INFO):
        run_app(sample_config)
    assert "Application started successfully!" in caplog.text
    assert f"Environment: {sample_config.app.environment}" in caplog.text


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
