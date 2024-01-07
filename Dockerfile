FROM python:3.11

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000
CMD gunicorn domain:app & python3 __main__.py
