FROM python:3.9-slim

#WorkDIR ?

COPY DataIngestion.py . 

RUN pip install OS 
RUN pip install pandas

EXPOSE 8080

ENTRYPOINT [ "python"]
CMD ["DataIngestion.py"]