FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1


# Update packages repository database
RUN apt-get update 

# Install cron to manage cron jobs
RUN apt-get install -y cron


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && rm -rf /app/requirements.txt 

COPY ./docker/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

WORKDIR /app
