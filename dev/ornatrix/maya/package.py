# An example of a package referencing something from outside
# of the local package.
name = "orn4maya"
version = "3.2.2"

authors = ['Ornatrix']

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

    env.ORNATRIX_GROOMS_DIR.append("{root}/resources/Data/Ephere/Grooms")
    env.ORNATRIX_PRESET_DIR.append("{root}/resources/Data/Ephere/CurvePresets")
    env.ORNATRIX_SCRIPTS_DIR.append("{root}/resources/Data/Ephere/Scripts")

    env.MAYA_MODULE_PATH.append("{root}/resources/modules")
