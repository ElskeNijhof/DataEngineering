# define Python version
FROM python:3.9-slim
#define workdir
WORKDIR /usr/src/myapp
# Copy requirements.txt  to the working directory
COPY requirements.txt .
# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt
#Copying JSON file(database) and Python files
COPY . .

#Expose the port that our app runs in
EXPOSE 5000

# Meta Data 
LABEL DataIngestion = "LocalVersion"
# Run our App
CMD [ "python3", "app.py"]
