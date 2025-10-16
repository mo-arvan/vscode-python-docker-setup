# Development Dockerfile
# This image is optimized for development with all necessary tools

FROM python:3.13-slim-bookworm

# it is best practice to pin to a specific uv version
# https://github.com/astral-sh/uv/pkgs/container/uv
# at the time of writing, the latest version is 0.6.14
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system dependencies for development
# Add any additional tools your development workflow needs here
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files for initial setup
# The actual code will be mounted as a volume by devcontainer
COPY pyproject.toml uv.lock* ./

# Sync dependencies including dev dependencies
# Note: This will be run again by postCreateCommand with mounted code
RUN uv sync || true

# Create non-root user for development
RUN useradd -ms /bin/bash appuser && \
    chown -R appuser:appuser /app

USER appuser

# Add virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Default command for development
CMD ["/bin/bash"]
