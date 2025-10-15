# Python Project Template

A template for Python projects using Docker, `uv`, and Hydra, with a focus on a consistent and reproducible environment.

## The Why: Philosophy & Tools

This template is built on a set of modern tools chosen to solve common problems in Python development:

- **Why Docker?** To ensure consistency between development and production environments. What works on your machine will work in deployment.
- **Why `uv`?** For extremely fast dependency management. It replaces `pip` and `venv` with a single, high-performance tool.
- **Why Hydra?** For flexible and powerful configuration. It allows you to manage complex configurations, automatically handles logging, and manages output directories.
- **Why Dev Containers?** For a seamless development experience. It lets you define your development environment as code, ensuring every team member has the exact same setup.

## The How: Practical Guide

### Requirements

- **Docker and Docker Compose** (Required)
- **Visual Studio Code** with the **[Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)** extension (Recommended for the intended development workflow).

### Development Workflow

1. **Clone the repository and open it in VS Code.**
2. When prompted, select **"Reopen in Container"**. This builds the dev container and uses `uv pip sync` to install all dependencies from `pyproject.toml`.
3. **Run the application:**

   ```bash
   uv run python src/main.py
   ```

4. **Run tests:**

   ```bash
   pytest
   ```

### Configuration

Configuration is split into two parts:

- **`conf/config.yaml`**: For non-sensitive application settings, managed by Hydra.
- **`.env` file**: For secrets and environment-specific variables. Copy `.env.example` to `.env` to get started.

### Deployment Workflow

1. The `Dockerfile` creates a production-ready image. It uses `uv sync` with the `uv.lock` file to guarantee a reproducible build with exact dependency versions.
2. To build and run the image, use Docker Compose:

   ```bash
   docker-compose up --build
   ```

## Customizing the Template

To adapt this template for your own project, you'll want to update the project name in the following files:

- **`pyproject.toml`**: Update the `name` field under the `[project]` section. This is the official name of your Python package.
- **`.devcontainer/devcontainer.json`**: Update the `name` field. This sets the name of the dev container.

After changing the name in `pyproject.toml`, you should regenerate the lock file to ensure consistency:

```bash
uv pip compile pyproject.toml -o uv.lock
```

## Technical Details & Design Decisions

This section explains the reasoning behind some of the key architectural choices in this template.

- **Development vs. Production Environments**: The setup intentionally separates the development environment from the production build. The `.devcontainer` is for a rich, interactive development experience inside VS Code, while the `Dockerfile` and `docker-compose.yml` are optimized for creating a lean, reproducible production image.

- **Dependency Management**: The template uses two different `uv` commands for a reason. In the dev container, `uv pip sync` (or `uv pip install -e .[test]`) is used to install dependencies directly from `pyproject.toml`, ensuring the environment always has the latest packages for development. In the `Dockerfile`, `uv sync` is used with the `uv.lock` file to guarantee that production builds are reproducible with exact package versions.

- **Configuration Strategy**: Configuration is split into two layers. `conf/config.yaml` is for non-sensitive, version-controlled settings. The `.env` file is for secrets and environment-specific values that should not be committed to version control.

- **`uv run` for Execution**: The `CMD` in the `Dockerfile` and the `command` in `docker-compose.yml` use `uv run`. This is a deliberate choice to ensure that the application always runs within the context of the `uv`-managed virtual environment, avoiding potential issues with `PATH` and environment variables.

- **Testability**: The core logic in `src/main.py` is intentionally separated from the `@hydra.main` decorator. This pattern makes the application's logic straightforward to import and test directly, without needing to involve Hydra in the unit tests.
