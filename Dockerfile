# --- Stage 1: Base Image ---
# Use an official, lightweight Python image
FROM python:3.10-slim

# --- Stage 2: Setup Environment ---
# Set the working directory inside the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# --- Stage 3: Install Dependencies ---
# Copy *only* the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install system dependencies (if any) and Python dependencies
# We use --no-cache-dir to keep the image slim
RUN pip install --no-cache-dir -r requirements.txt

# --- Stage 4: Copy Application Code ---
# Copy the rest of the application code
# This includes our 'py_deep_dive' package and 'main.py'
COPY . .

# --- Stage 5: Define Entry Point ---
# This is the command that will run when the container starts
# It's equivalent to running `python3 main.py` in the terminal
CMD ["python3", "main.py"]
