#!/bin/bash

apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
apk add --update --no-cache py3-pip && pip install kafka-python

python3 producer.py $KAFKA_HOST