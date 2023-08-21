FROM python:3.9-slim

ENV RUNNING_IN_DOCKER=true

WORKDIR /app

COPY app_test.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app_test.py"]

