FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 ca-certificates -y
RUN pip install scikit-image
RUN pip install opencv-python
RUN pip install colorthief
RUN pip install requests


ENV LISTEN_PORT 8097

COPY ./app /app