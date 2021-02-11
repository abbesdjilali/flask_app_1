FROM alpine
COPY . /app
WORKDIR /app
ENV FLASK_APP=home.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk --update add bash python3 vim py-pip
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
ENTRYPOINT [ "python3" ]
EXPOSE 5050
CMD ["home.py"]