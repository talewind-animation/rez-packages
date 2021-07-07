name = "ffmpeg"
version = "4.4.0"
requires = [
        "quicktime",
    ]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

authors = ["John Van Sickle", "Joseph Yu"]

tools = [
    "ffmpeg",
]

variants = [
    ["platform-windows"]
]

description = """
A complete, cross-platform solution to record, convert and stream audio and video."""


def commands():
    global env

    env.PATH.append("{root}/resources")
