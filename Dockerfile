FROM python:3.8.12-buster AS base

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 86
WORKDIR /app
ENTRYPOINT ["streamlit","run","app.py","--server.port=86"]