# An example of a package referencing something from outside
# of the local package.
name = "mtoa"
version = "4.2.2"

authors = ['SolidAngle']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "rlm",
    "~maya-2020",
]

description = """
Arnold is an advanced Monte Carlo ray tracing renderer
built for the demands of feature-length animation and visual effects."""

variants = [
    ["maya-2020"],
]

tools = [
    'kick',
    'oslc',
    'oslinfo',
    'maketx'
]

plugin_for = ["maya"]

def commands():
    global env

    env.PATH.append("{root}/resources/bin")
    env.MAYA_MODULE_PATH.append("{root}/resources")
    env.MTOA_EXTENSIONS_PATH.append("{root}/resources/extensions")
