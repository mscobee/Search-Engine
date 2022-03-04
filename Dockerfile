FROM ubuntu:latest
FROM python:latest
WORKDIR /src
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get clean
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]