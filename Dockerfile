# Base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project code
COPY . /app

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
