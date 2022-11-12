FROM alpine
RUN apt install python3 -y
RUN mkdir /app && rm /app/*
COPY new.py /app