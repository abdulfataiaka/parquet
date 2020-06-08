FROM python:3.7-alpine

RUN apk --update add \
    curl \
    bash \
    gcompat \
    openjdk8-jre

WORKDIR /spark

COPY . .

RUN bin/spark-install
ENV SPARK_HOME="/opt/spark"
ENV PATH="/opt/spark/bin:$PATH"
ENV PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
ENV PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH"

CMD [ "pyspark", "--version" ]
