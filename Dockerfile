FROM python:3.10.2
WORKDIR /app
COPY ./src ./
RUN ["pip", "install", "-r", "requirements.txt"]
ENTRYPOINT ["python", "-u", "main.py"]