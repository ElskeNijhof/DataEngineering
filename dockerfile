FROM python:3.9-slim

COPY Predict.py .
COPY Titanic_model.pkl .

RUN pip install sklearn #Package die nodig is voor het model (Predict.py)

#ENTRYPOINT [ "/bin/bash" ] # terminal meteen opstarten

# Build image
# docker run -it titanicpredict (image name)

ENTRYPOINT [ "python" ,"Predict.py" ]
