FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install python3-pip -y 
RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
