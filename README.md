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

### Docker Files

This template uses separate Dockerfiles for different purposes:

- **`dev.Dockerfile`**: Used by the dev container (`.devcontainer/devcontainer.json`)
  - Includes `uv` for managing dependencies
  - Includes `git` and other development tools
  - Installs all dependencies including dev dependencies (pytest, etc.)
  - Optimized for development workflow
  
- **`python.Dockerfile`**: Used for production deployment (`docker-compose.yml`)
  - Multi-stage build for optimized image size
  - Excludes development dependencies and tools
  - Only includes runtime dependencies and application code
  - **Important**: Modify this file to add any system dependencies your application needs at runtime (e.g., database clients, image processing libraries, etc.)

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
   uv sync
   ```

## Production Docker Image

The `python.Dockerfile` uses a multi-stage build approach for optimized production images:

- **Builder stage**: Installs dependencies using `uv` with the frozen lockfile
- **Production stage**: Contains only the runtime environment and application code
- **Benefits**: Smaller image size, faster deployments, excludes development dependencies and test files

### Customizing for Production

The production Dockerfile is intentionally minimal. You'll likely need to customize it based on your application's requirements:

**Common modifications to the production stage:**

```dockerfile
# Example: Add system dependencies for data science libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \           # PostgreSQL client library
    libgomp1 \         # Required by some ML libraries
    && rm -rf /var/lib/apt/lists/*

# Example: Add health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Example: Expose ports for web services
EXPOSE 8000
```

**Remember:** Only add what your application actually needs at runtime. Development tools should go in `dev.Dockerfile`.

## Logging

Logging is automatically configured by Hydra based on `conf/config.yaml`. You can:

- Adjust log levels in the config file
- Override at runtime: `uv run python src/main.py logging.level=DEBUG`
- Hydra automatically creates timestamped output directories for each run

## Potential Enhancements

Depending on your project's complexity and requirements, consider adding:

### For Larger Projects

- **CI/CD Pipeline**: GitHub Actions or GitLab CI for automated testing and deployment
- **Pre-commit Hooks**: Code formatting and linting checks before commits
- **API Layer**: FastAPI or Flask for building REST APIs
- **Database Integration**: SQLAlchemy for database operations

### For ML/Data Science Projects

- **ML Dependencies**: Add NumPy, scikit-learn, PyTorch, or TensorFlow as needed
- **Experiment Tracking**: MLflow, Weights & Biases, or similar tools
- **Data Management**: DVC for data version control, structured data directories
- **Notebooks**: Jupyter notebooks for exploratory data analysis
- **Model Management**: Model versioning and serialization strategies

### For Production Systems

- **Monitoring**: Application performance monitoring and observability
- **Security**: Dependency scanning with safety or bandit
- **Health Checks**: Docker health check configurations
- **Container Registry**: Push images to Docker Hub, GitHub Container Registry, etc.

Most hobby projects don't require all these features from day one. Start simple and add complexity as your project grows.
