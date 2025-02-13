# Use a lightweight Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "loan_app.py"]
