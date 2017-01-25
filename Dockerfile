FROM python:3-alpine

MAINTAINER Joe Black <joeblack949@gmail.com>

ENV     KUBEWAIT_VERSION 0.2.1

LABEL   lang.python.version=3
LABEL   app.name=kubewait \
        app.version=${KUBEWAIT_VERSION}

ADD     https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /dumb-init
RUN     chmod +x /dumb-init

RUN     pip3 install kubewait

ENV     ENVIRONMENT production
ENV     LOG_LEVEL INFO
ENV     NAMESPACE default
ENV     DOMAIN cluster.local

ENTRYPOINT  ["/dumb-init", "--", "kubewait"]
