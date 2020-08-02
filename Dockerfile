FROM python:3.6-slim

RUN groupadd -g 999 app && \
    useradd -r -u 999 -g app app

RUN mkdir /todoapp
WORKDIR /todoapp

ADD app ./app
ADD LICENSE .
ADD requirements.txt .
ADD README.MD .
ADD setup.py .
RUN pip install .
RUN rm -rf *

ADD gunicorn.py .
ADD logging.conf .
ADD startup.sh .

ARG VERSION
ENV API_VERSION=$VERSION

ENV FLASK_APP "todoapp"
EXPOSE 5000

CMD ./startup.sh
