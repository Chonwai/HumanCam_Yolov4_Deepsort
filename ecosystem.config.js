module.exports = {
    apps: [
        {
            name: 'HumanCamYolo',
            instances: 1, // Or a number of instances
            cmd: "object_tracker.py",
            args: "-weights './checkpoints/yolov4-tiny-416/' -model yolov4 -tiny True -video 'rtsp://admin:a1111111@192.168.14.248/Streaming/Channels/2' -output './data/outputs/' -dont_show True -output_format MP4V",
            interpreter: 'python3',
            watch: true,
            autorestart: true,
        }
    ]
};
