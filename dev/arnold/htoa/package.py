
name = "htoa"
version = "5.6.3"

authors = ['SolidAngle']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "rlm",
    "~houdini",
]

description = """
Arnold is an advanced Monte Carlo ray tracing renderer
built for the demands of feature-length animation and visual effects."""

variants = [
    ["houdini-18.5.596"],
]

plugin_for = ["houdini"]

def commands():
    global env

    env.PATH.append("{root}/resources/scripts/bin")
    env.HOUDINI_PATH.prepend("{root}/resources")
