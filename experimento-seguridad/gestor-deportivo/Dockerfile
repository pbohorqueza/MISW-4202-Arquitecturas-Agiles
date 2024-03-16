FROM python:3.11-slim-buster
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["./run.sh"]
EXPOSE 3001