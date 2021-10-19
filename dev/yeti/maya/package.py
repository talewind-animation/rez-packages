# An example of a package referencing something from outside
# of the local package.
name = "yeti4maya"
version = "4.0.4"

authors = ['Peregrine Labs']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "maya-2020",
]

description = """
A powerful node based procedural toolset for producing fur, feathers and efficiently instancing geometry.
"""

plugin_for = ["maya"]

def commands():
    global env

    env.MAYA_MODULE_PATH.append("{root}/resources/modules")
