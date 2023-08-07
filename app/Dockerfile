FROM nginx:stable-bullseye

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

COPY . /app
WORKDIR /app

ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR; exit 0

RUN pip3 install -r requirements.txt

EXPOSE 5001/tcp

CMD ["/bin/bash", "-c", "source .env && python3 app.py"]
