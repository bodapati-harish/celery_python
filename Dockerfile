# Use Python slim image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*  # <-- Ensure this is on the same line as `git \`

# Create non-root user
RUN useradd -m -u 1001 appuser

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .
RUN git --version  # <-- Optional: Check if git is installed (for debugging)
RUN pip install --no-cache-dir -r requirements.txt
