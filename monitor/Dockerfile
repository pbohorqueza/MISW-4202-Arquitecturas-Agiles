FROM python:3.11-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "run-tasks.sh", "&&", "run_celery.sh" ]