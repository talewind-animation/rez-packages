name = "aces"
version = "1.2.0"
requires = []

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]


def commands():
    global env

    env.OCIO = "{root}/resources/config.ocio"

