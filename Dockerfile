FROM alpine
RUN apk update && apk upgrade --available \
    apk add --update python3 \
    python3 -V
RUN mkdir /app && rm /app/*
COPY new.py /app