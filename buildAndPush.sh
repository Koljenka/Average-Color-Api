#!/bin/bash
VERSION=1.1.1
docker build -t kojenka/avg-color-api:$VERSION .
docker tag kojenka/avg-color-api:$VERSION kojenka/avg-color-api:latest
docker push kojenka/avg-color-api:$VERSION
docker push kojenka/avg-color-api:latest
