FROM nvcr.io/nvidia/pytorch:19.10-py3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -qq && apt-get install -y \
    tmux pylint && \
    rm -rf /var/lib/apt/lists/*

RUN pip install flake8 flake8-mypy flake8-bugbear flake8-comprehensions flake8-executable flake8-pyi mccabe pycodestyle pyflake bandit black

# autopep8
RUN mkdir -p /root/.ssh/ && ssh-keyscan github.com >> /root/.ssh/known_hosts