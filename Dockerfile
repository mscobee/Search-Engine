# FROM ubuntu:latest
FROM python:latest
RUN mkdir -p /home/app
WORKDIR /home/app
COPY . /home/app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader stopwords
CMD ["python", "engine/main.py"]
