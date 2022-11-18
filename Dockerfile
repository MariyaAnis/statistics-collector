FROM python:3.10-slim
WORKDIR /app
RUN apt update && apt -y install libpq-dev build-essential
COPY requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "--bind", "0:8000", "collector.wsgi:application"]