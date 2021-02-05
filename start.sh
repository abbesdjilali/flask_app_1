#!/bin/bash
app_test="docker.flask"
docker build -t ${app_test} .
docker run -d -p 5050:5050 --name=${app_test} ${app_test}