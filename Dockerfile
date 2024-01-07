FROM python:3.11

WORKDIR /app
COPY . /app/

RUN apt-get update && apt-get install -y tree
RUN tree

RUN pip install -r requirements.txt

EXPOSE 8000
CMD gunicorn web/domain:app & python3 main.py
