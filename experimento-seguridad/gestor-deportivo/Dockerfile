FROM python:3.11-slim-buster
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD * /app/
ENTRYPOINT ["./run.sh"]
EXPOSE 3001