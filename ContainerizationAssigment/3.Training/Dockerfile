#using python as base image
FROM python:3.9-slim
#set work directory
WORKDIR /myapp
# Get all files in this directory
COPY . .
#install packages
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install sklearn 
#expose to port 500
EXPOSE 500
# define URL needed for Feature extraction
#ENV FEATURE_API = http://FeatureExtractions:500/2.FeatureExtractions/DatabaseFeatures

CMD ["python" ,"app2.py" ] 


