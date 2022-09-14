FROM alpine:latest
RUN apk update 
RUN apk add  python3 py3-pip
#RUN pip install requests --user 

RUN mkdir app
COPY requirements.txt  /app/requirements.txt
COPY authentication.py  /app/authentication.py 

WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "authentication.py"] 
