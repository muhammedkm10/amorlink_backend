# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Upgrade pip and install production dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Copy the rest of the application code
COPY . .

# Expose the necessary port
EXPOSE 8000

# Start Gunicorn
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "backend.asgi:application"]
