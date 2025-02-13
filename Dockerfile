# Use an official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY loan_app.py .
COPY loan_disbursement.py .

# Install any required dependencies (if any, add a requirements.txt file)
RUN pip install -r requirements.txt

# Command to run the app
CMD ["python", "loan_app.py"]
