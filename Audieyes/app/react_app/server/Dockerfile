# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary directory contents into the container at /app
COPY . /app

# Install PyTorch and other dependencies
RUN pip install --no-cache-dir torch torchvision torchaudio \
    flask flask-cors pillow transformers

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
