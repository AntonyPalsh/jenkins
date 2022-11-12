FROM alpine
RUN RUN apk add --no-cache curl wget busybox-extras netcat-openbsd python py-pip && \
    pip install awscli && \ 
    apk --purge -v del py-pip
RUN mkdir /app && rm /app/*
COPY new.py /app