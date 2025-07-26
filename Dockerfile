FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1


# Set working directory
WORKDIR /src



# Install poetry
RUN pip install poetry

# Copy poetry configuration files
COPY pyproject.toml ./
RUN poetry install --no-interaction --no-ansi --no-root


# Copy source code
COPY . .

