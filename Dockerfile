# Use Python 3.10-slim as base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    CHROME_BIN=/usr/bin/google-chrome-stable \
    TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata \
    PYTESSERACT_PATH=/usr/bin/tesseract

# Install essential packages for repository setup
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    gnupg \
    jq \
    file \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add the necessary configuration for using nvidia ollama and Google Chrome
RUN curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
    | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -sL https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
    | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
    | tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
    && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor -o /usr/share/keyrings/google-chrome-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    | tee /etc/apt/sources.list.d/google-chrome.list

# Install system dependencies including those for Tesseract OCR, spaCy, and Chrome
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    g++ \
    tesseract-ocr \
    tesseract-ocr-por \
    libtesseract-dev \
    libleptonica-dev \
    pkg-config \
    git \
    nvidia-container-toolkit \
    google-chrome-stable \
    fonts-liberation \
    libxss1 \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libgbm1 \
    libnss3 \
    libx11-xcb1 \
    libxtst6 \
    xdg-utils \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -m spacy download pt_core_news_sm

# Install chrome-for-testing binary to handle version 136
RUN set -e \
    && echo "Getting Chrome version..." \
    && CHROME_VERSION=$(google-chrome-stable --version | awk '{print $3}') \
    && echo "Chrome version: $CHROME_VERSION" \
    && echo "Installing Chrome for Testing with compatible driver..." \
    && wget -q -O /tmp/chrome-linux.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/136.0.7103.113/linux64/chrome-linux64.zip" \
    && wget -q -O /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/136.0.7103.113/linux64/chromedriver-linux64.zip" \
    && echo "Downloaded Chrome for Testing packages" \
    && unzip -q /tmp/chrome-linux.zip -d /opt/ \
    && unzip -q /tmp/chromedriver.zip -d /tmp/ \
    && mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && chmod +x /opt/chrome-linux64/chrome \
    && ln -sf /opt/chrome-linux64/chrome /usr/local/bin/chrome-for-testing \
    && rm -rf /tmp/chrome-linux.zip /tmp/chromedriver.zip /tmp/chromedriver-linux64 \
    && echo "Chrome for Testing installation completed." \
    && echo "Chrome for Testing path: /opt/chrome-linux64/chrome" \
    && echo "ChromeDriver version:" \
    && chromedriver --version

# Copy project files
COPY . .

# Collect static files
RUN mkdir -p /app/staticfiles

# Set permissions
RUN chmod +x manage.py

# Expose port for Django development server
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
