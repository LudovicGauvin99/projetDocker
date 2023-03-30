FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3 python3-pip
RUN pip install flask
RUN pip install mysql-connector-python  

WORKDIR /mnt/d/Hitema/cours devops/docker/

COPY ./app.py ./appCopy.py

CMD ["python3", "./appCopy.py"]
