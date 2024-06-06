# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 8888

# Define environment variable for the API keys
ENV HF_API_KEY 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
ENV HF_API_KEY_2 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

# Run main.py when the container launches
CMD ["python", "pepper_client/main.py"]
