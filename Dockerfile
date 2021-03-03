From python:3.7

COPY ./requirements.txt /opt/requirements.txt

WORKDIR /opt
RUN pip install -r requirements.txt
