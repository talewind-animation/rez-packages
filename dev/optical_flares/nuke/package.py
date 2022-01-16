# An example of a package referencing something from outside
# of the local package.
name = "optical_flares4nuke"
version = "1.0.86"

authors = ['VideoCopilot']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "~nuke-13",
]

description = """
VC OP"""

plugin_for = ["nuke"]

def commands():
    global env

    env.OPTICAL_FLARES_PATH = "{root}/resources/OpticalFlares"
    env.NUKE_PATH.append("{root}/resources/plugin")
