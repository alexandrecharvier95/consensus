FROM python:3.14-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.4.30 /uv /uvx /usr/local/bin/
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV UV_LINK_MODE=copy

# Install Node.js (required by Reflex for the frontend build)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    nodejs \
    npm \
    unzip \
    && rm -rf /var/lib/apt/lists/*

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

ENV REFLEX_FRONTEND_PORT=3000
ENV REFLEX_BACKEND_PORT=8001
ENV REFLEX_API_URL="http://localhost:${REFLEX_BACKEND_PORT}"

EXPOSE ${REFLEX_FRONTEND_PORT}

CMD ["uv", "run", "reflex", "run"]
