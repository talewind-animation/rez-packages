# An example of a package referencing something from outside
# of the local package.
name = "ktoa"
version = "3.2.2"

authors = ['SolidAngle']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "~katana-4.0",
    "rlm",
]

description = """
Arnold is an advanced Monte Carlo ray tracing renderer
built for the demands of feature-length animation and visual effects."""

variants = [
    ["katana-4.0"],
]

plugin_for = ["katana"]

def commands():
    global env

    env.KTOA_HOME = "{root}/resources"
    env.PATH.append("{root}/resources/bin")
    env.PYTHONPATH.append("{root}/resources/python")
    env.KATANA_RESOURCES.append("{root}/resources")
    env.DEFAULT_RENDERER="arnold"
