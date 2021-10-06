FROM python:3.9-slim

COPY Train.py .

RUN pip install sklearn #Package die nodig is voor het model (Train.py)

EXPOSE 5000 

#ENTRYPOINT [ "/bin/bash" ] # terminal meteen opstarten

# Build image
# docker run -it titanicpredict (image name)

ENV FEATURE_API = http://FeatureExtractions:5000/2.FeatureExtractions/DatabaseFeatures

CMD ["python" ,"Train.py" ] # ENTRYPOINTonly excutable


