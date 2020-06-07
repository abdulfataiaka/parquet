FROM python:3.7-alpine

RUN apk --update add \
    curl \
    bash \
    openjdk8-jre

WORKDIR /spark

COPY . .

RUN bin/spark-install
ENV PATH="/opt/spark/bin:$PATH"

CMD [ "pyspark", "--version" ]
