FROM python:3.13-slim-bookworm

# it is best practice to pin to a specific uv version
# https://github.com/astral-sh/uv/pkgs/container/uv
# at the time of writing, the latest version is 0.6.14
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*


# Copy the project into the image
ADD . /app
WORKDIR /app

# Sync the project into a new environment, using the frozen lockfile
RUN uv sync


# add a non-root user
RUN useradd -ms /bin/bash appuser
USER appuser

ENV PATH="/app/.venv/bin:$PATH"


# Default command - can be overridden in docker-compose.yml or at runtime
CMD ["uv", "run", "python", "src/main.py"]
