# Using python 3.7 slim image as the base image
FROM python:3.9-slim
# Defining working directory and copy the requirements file. We will run the commands inside this new directory
WORKDIR /usr/src/myapp
# Copy requirements.txt  to the working directory
COPY requirements.txt /usr/src/myapp/
# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install sklearn
# Copy all files in training-db local host directory to /usr/src/myapp in Docker container
COPY . .
# Expose the port that our app runs in
EXPOSE 5000
# Environment  Variables
ENV TRAININGDB_API=http://DataIngestion:5000/DataIngestion/database


# Run our App
CMD ["python3","app.py"]