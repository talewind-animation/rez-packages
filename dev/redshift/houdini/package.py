name = "redshift4houdini"
version = "3.0.45"

authors = ['Redshift']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "redshift_core-{}".format(version),
    "~houdini>=17.0.506|<18.5.596",
]

description = """
Redshift is an award-winning, production ready GPU renderer for fast 3D rendering"""

plugin_for = ["houdini"]

def commands():
    import os
    global env

    houdini_version = env.HOUDINI_VERSION.value()
    redshift_root = env.REDSHIFT_COREDATAPATH.value()

    env.HOUDINI_DSO_ERROR = 2
    env.PATH.append(r"{}/bin".format(redshift_root))
    env.HOUDINI_PATH.prepend(r"{}/Plugins/Houdini/{}".format(redshift_root, houdini_version))
    if not os.getenv("PXR_PLUGINPATH_NAME"):
        env.PXR_PLUGINPATH_NAME = "&"
    env.PXR_PLUGINPATH_NAME.prepend(r"{}/Plugins/Solaris/{}".format(redshift_root, houdini_version))
