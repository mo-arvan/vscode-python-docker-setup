FROM python:3.13-slim-bookworm

# it is best practice to pin to a specific uv version
# https://github.com/astral-sh/uv/pkgs/container/uv
# at the time of writing, the latest version is 0.6.14
COPY --from=ghcr.io/astral-sh/uv:0.6.14 /uv /uvx /bin/


# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*


# Copy the project into the image
ADD . /app
# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app

RUN uv sync


# add a non-root user
RUN useradd -ms /bin/bash appuser
USER appuser

ENV PATH="/app/.venv/bin:$PATH"


# Presuming there is a `my_app` command provided by the project
CMD ["python", "src/benchmark.py"]
