# Python Project Template

A template for Python projects using Docker, `uv`, and Hydra, with a focus on a consistent and reproducible environment.

## Getting Started

### Requirements

- **Docker and Docker Compose**
- **Visual Studio Code** with the **[Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)** extension. (Recommended for the intended development workflow).

### Setup

1. **Start a new project**: Download this repository as a ZIP file and extract it to your new project folder.
2. **Rename the project**: Change the project folder as well as project name in `pyproject.toml` and `.devcontainer/devcontainer.json` to your desired project name.
3. **Git Initialization**: Initialize a new Git repository in your project folder if needed.
4. **Open in VS Code**: Open the project folder in Visual Studio Code.
5. **Reopen in Container**: When prompted, select **"Reopen in Container"**. This uses the `.devcontainer/devcontainer.json` configuration to build a consistent development environment with Docker. It will automatically install all dependencies from `pyproject.toml` for you.

### Development Cycle

- **Run the application**:

  ```bash
  uv run python src/main.py
  ```

- **Run tests**:

  ```bash
  pytest
  ```

## Key Concepts

### Configuration

Configuration is managed in two places:

- **`conf/config.yaml`**: For non-sensitive application settings, managed by [Hydra](https://hydra.cc/). Hydra also automatically handles logging and output directories based on this file.
- **`.env`**: For secrets and environment-specific variables. Copy `.env.example` to `.env` to get started.

### Dependency Management

This template uses [uv](https://github.com/astral-sh/uv) for high-performance dependency management.

- **For Development**: The dev container uses `uv sync` to keep your environment up-to-date with `pyproject.toml`.
- **For Production**: The `Dockerfile` uses `uv sync` with the `uv.lock` file to create a reproducible build with pinned dependencies.

### Deployment

To create a production-ready build, use Docker Compose:

```bash
docker compose up --build
```

This command uses the `Dockerfile` to build a self-contained image and run it.

## Customization

To make this template your own:

1. **Set your project name** in `pyproject.toml` and `.devcontainer/devcontainer.json`.
2. **Regenerate the lock file** to reflect the new name:

   ```bash
   uv pip compile pyproject.toml -o uv.lock
   ```
