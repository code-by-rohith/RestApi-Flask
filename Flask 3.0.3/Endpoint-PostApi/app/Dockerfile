# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app.py .

# Expose the port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]



# docker build -t flask-app .
# docker run -p 5005:5000 flask-app  ---> run docker container
#docker run -dp 5005:5000 flask-app   ---> run docker container in backround
#docker-compose up -d ----> run flask and mongo in backround
#docker-compose up   -----> run flask and mongo


