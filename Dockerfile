FROM python:3.5
RUN apt update && apt install -y gettext
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

ADD wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
