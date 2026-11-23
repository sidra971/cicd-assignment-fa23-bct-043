
FROM python:3.12-slim

# Install Chromium browser and its driver
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install Selenium
RUN pip install --no-cache-dir -r requirements.txt

# Copy application and tests
COPY index.html .
COPY test_app.py .

# Run Selenium tests
CMD ["python", "-m", "unittest", "-v", "test_app"]
