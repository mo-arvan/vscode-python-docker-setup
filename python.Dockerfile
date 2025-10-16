FROM python:3.13-slim-bookworm AS builder

# it is best practice to pin to a specific uv version
# https://github.com/astral-sh/uv/pkgs/container/uv
# at the time of writing, the latest version is 0.6.14
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy the project files needed for dependency resolution
COPY pyproject.toml uv.lock ./

# Copy source code (but not tests or other unnecessary files)
COPY src ./src
COPY conf ./conf

# Sync the project into a new environment, using the frozen lockfile
RUN uv sync --frozen --no-dev


# Production stage
FROM python:3.13-slim-bookworm

# Install only runtime system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only the virtual environment from builder
COPY --from=builder /.venv /app/.venv

# Copy application code
COPY src ./src
COPY conf ./conf

# add a non-root user
RUN useradd -ms /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

ENV PATH="/app/.venv/bin:$PATH"

# Default command - can be overridden in docker-compose.yml or at runtime
CMD ["python", "src/main.py"]
