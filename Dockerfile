# only for render deployment: @nabilanavab

FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y tree
RUN tree

EXPOSE 8000
CMD ["gunicorn", "web.domain:app", "&", "python3", "web/main.py"]
