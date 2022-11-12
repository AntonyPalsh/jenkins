FROM alpine
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN mkdir /app
COPY new.py /app
WORKDIR /app
RUN python3 new.py