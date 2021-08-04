# An example of a package referencing something from outside
# of the local package.
name = "animation_tools"
version = "0.1.0"

authors = ['Tale Wind']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "~maya-2022+",
]

description = """
Scripts and tools for animators.
"""

plugin_for = ["maya"]

def commands():
    global env

    env.MAYA_PLUG_IN_PATH.append("{root}/resources/picker")
    env.PYTHONPATH.append("{root}/resources/studiolibrary")
