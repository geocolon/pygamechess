# Step 1: Use a lightweight Python image
FROM python:3.9-slim

# Step 2: Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    xvfb

# Step 3: Create and set the working directory inside the container
WORKDIR /app

# Step 4: Copy local files to the container's working directory
COPY . /app

# Step 5: Install Python dependencies
RUN pip install pygame

# Step 6: Install X virtual framebuffer to simulate display for pygame
RUN apt-get install -y xvfb

# Step 7: Start the X virtual framebuffer in the background when the container starts
CMD ["xvfb-run", "--auto-servernum", "--server-args=-screen 0 800x600x24", "python", "client.py"]
