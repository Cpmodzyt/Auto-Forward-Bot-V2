# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (if applicable)
EXPOSE 8000

# Set the default command to run the application
CMD ["python", "main.py"]
