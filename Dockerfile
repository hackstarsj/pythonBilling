# Using a official Python Runting
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into docker image
COPY . /app

# Run the Program.py file
CMD ["python", "Program.py"]
