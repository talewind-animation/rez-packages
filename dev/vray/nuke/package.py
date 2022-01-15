# An example of a package referencing something from outside
# of the local package.
name = "vray4nuke"
version = "5.20.00"

authors = ['Choas Group']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "nuke-13.0",
]

description = """
    Production-proven ray traced rendering with a full suite of tools
    to create professional photoreal imagery and animations."""

tools = [
    "vray",
]

plugin_for = ["maya"]

def commands():
    global env

    nuke_version = 13

    env["VRAY_FOR_NUKE_{}_PLUGINS ".format(nuke_version)] = "{root}/resources/nuke_vray"
    env.VRAY_RT_GPU_LIBRARY_PATH = "{root}/resources/vray_std"
    env.NUKE_PATH = "{root}/resources/nuke_plugins"
    env["PATH"].append("{root}/resources/nuke_root")
