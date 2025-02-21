# Use a lightweight Python image
FROM python:3.9-slim  

# Set the working directory inside the container
WORKDIR /app  

# Copy only requirements first to leverage Docker's caching
COPY requirements.txt requirements.txt  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the rest of the application files
COPY . .  

# Expose the port Flask/Gunicorn will run on
EXPOSE 5000  

# Start the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
