FROM python:3.9.10
WORKDIR /app
COPY ./src ./
RUN ["pip", "install", "-r", "requirements.txt"]
CMD ["python", "-u", "main.py"]