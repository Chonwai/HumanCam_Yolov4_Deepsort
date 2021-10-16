module.exports = {
    apps: [
        {
            name: 'HumanCamYolo',
            instances: 1, // Or a number of instances
            cmd: "object_tracker.py",
            args: "arg1 arg2 arg3 arg4 arg5 arg6 arg7",
            interpreter: 'python3',
            watch: true,
            autorestart: true,
        }
    ]
};
