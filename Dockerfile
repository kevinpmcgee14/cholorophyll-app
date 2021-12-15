FROM python:3.8-buster
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/cholorphyll_app
WORKDIR /opt/cholorphyll_app
COPY . .

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y apt-transport-https

RUN pip3.8 install -r requirements.txt
RUN pip3.8 install gunicorn

CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
