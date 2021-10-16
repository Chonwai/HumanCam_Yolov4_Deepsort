FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install opencv-python-headless

ENV YOLO_ROOT /yolo
RUN mkdir $YOLO_ROOT
WORKDIR /yolo

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]