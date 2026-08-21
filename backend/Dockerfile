FROM python:3.14-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.4.30 /uv /uvx /usr/local/bin/

WORKDIR /app

# Copy dependency files first for layer caching
COPY pyproject.toml .
COPY uv.lock* .

# Install dependencies (without installing the project itself)
RUN uv sync --frozen --no-dev --no-install-project

# Copy application code
COPY . .

# Install the project
RUN uv sync --frozen --no-dev

ENV UVICORN_HOST="0.0.0.0"
ENV UVICORN_PORT="8000"

EXPOSE ${UVICORN_PORT}

CMD ["uv", "run", "uvicorn", "consensus_backend.main:app"]
