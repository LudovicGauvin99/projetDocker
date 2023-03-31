FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3 python3-pip
RUN apt-get install -y libmysqlclient-dev
RUN pip install flask 
RUN pip install flask-MySQLdb

WORKDIR /mnt/d/Hitema/cours devops/docker/

COPY ./app.py ./appCopy.py

CMD ["python3", "./appCopy.py"]
