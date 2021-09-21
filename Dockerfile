FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV YOLO_ROOT /yolo
RUN mkdir $YOLO_ROOT
WORKDIR /yolo

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]

# CMD ["python", "./object_tracker.py", "--weights", "./checkpoints/yolov4-tiny-trt-int8/", "--model", "yolov4", "--video", "0", "--tiny"]

# python object_tracker.py --weights ./checkpoints/yolov4-tiny-trt-int8/ --model yolov4 --video ./data/video/walking_fps3.mp4 --output ./outputs/walking_fps3.mp4 --tiny