FROM python:3.10.2-bullseye

ADD engine .

RUN pip install requests beautifulsoup4 mariadb lxml nltk

CMD ["python", "./main.py"]