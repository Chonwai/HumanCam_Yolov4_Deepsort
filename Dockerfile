FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install opencv-python-headless

# RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
# RUN apt-get install nodejs
# RUN node -v
# RUN npm install pm2 -g

ENV YOLO_ROOT /yolo
RUN mkdir $YOLO_ROOT
WORKDIR /yolo

COPY . .

# ENTRYPOINT ["bash", "entrypoint.sh"]
# CMD pm2-runtime start ecosystem.config.js