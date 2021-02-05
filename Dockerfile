FROM alpine
RUN apk --update add bash python3 vim py-pip
COPY . /app
WORKDIR /app
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5050
CMD ["home.py"]