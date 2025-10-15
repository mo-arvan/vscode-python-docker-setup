import logging

import hydra
from omegaconf import DictConfig

log = logging.getLogger(__name__)

def run_app(cfg: DictConfig) -> None:
    """Core application logic."""
    log.info("Application started successfully!")
    log.info(f"Environment: {cfg.app.environment}")

    # Your application logic starts here

@hydra.main(version_base=None, config_path="../conf", config_name="config")
def main(cfg: DictConfig) -> None:
    """
    Main application function.

    Args:
        cfg: Hydra configuration object
    """
    run_app(cfg)


if __name__ == "__main__":
    main()
