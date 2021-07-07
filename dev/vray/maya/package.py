# An example of a package referencing something from outside
# of the local package.
name = "vray"
version = "5.00.22"

authors = ['Choas Group']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "~maya",
]

description = """
    Production-proven ray traced rendering with a full suite of tools
    to create professional photoreal imagery and animations."""

variants = [
    ["maya-2017"],
    ["maya-2020"],
]

tools = [
    "vray",
]

plugin_for = ["maya"]

def commands():
    global env

    maya_version = env.MAYA_VERSION.value()

    env["VRAY_FOR_MAYA{}_MAIN".format(maya_version)] = "{root}/resources/maya_vray"
    env["VRAY_FOR_MAYA{}_PLUGINS".format(maya_version)] = "{root}/resources/maya_vray/vrayplugins"
    env["VRAY_OSL_PATH_MAYA{}".format(maya_version)] = "{root}/resources/vray/opensl"
    env["VRAY_PLUGINS"] = "{root}/resources/maya_vray/vrayplugins"
    env.VRAY_AUTH_CLIENT_FILE_PATH = "{root}/resources"
    env.VRAY_SEND_FEEDBACK = "0"

    env.PATH.append("{root}/resources/maya_root/bin")
    env.PATH.append("{root}/resources/vray/lib")
    env.MAYA_RENDER_DESC_PATH.append("{root}/resources/maya_root/bin/rendererDesc")
    env.MAYA_PLUG_IN_PATH.append("{root}/resources/maya_vray/plug-ins")
    env.MAYA_SCRIPT_PATH.append("{root}/resources/maya_vray/scripts")
    env.MAYA_PRESET_PATH.append("{root}/resources/maya_vray/presets")
    env.PYTHONPATH.append("{root}/resources/maya_vray/scripts")
    env.XBMLANGPATH.append("{root}/resources/maya_vray/icons")
