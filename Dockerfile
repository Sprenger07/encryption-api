FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ ./src

EXPOSE 8000

CMD [ "fastapi" , "run", "src/main.py"]