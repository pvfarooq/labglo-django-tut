FROM python:3.8-slim-buster

RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    git


COPY req.txt req.txt
RUN pip3 install -r req.txt --upgrade


COPY . .

CMD ["python3", "manage.py", "runserver","0.0.0.0:8001"]
