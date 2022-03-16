name = "redshift4maya"
version = "3.0.45"

authors = ['Redshift']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "redshift_core-{}".format(version),
    "~maya>=2014|<2022",
]

description = """
Redshift is an award-winning, production ready GPU renderer for fast 3D rendering"""

plugin_for = ["maya"]

def commands():
    import os
    global env

    maya_version = env.MAYA_VERSION.value()
    redshift_root = env.REDSHIFT_COREDATAPATH.value()

    env.REDSHIFT_PLUG_IN_PATH = r"{}/Plugins/Maya/{}/nt-x86-64".format(redshift_root, maya_version)
    env.REDSHIFT_SCRIPT_PATH = r"{}/Plugins/Maya/Common/scripts".format(redshift_root)
    env.REDSHIFT_XBMLANGPATH = r"{}/Plugins/Maya/Common/icons".format(redshift_root)
    env.REDSHIFT_RENDER_DESC_PATH = r"{}/Plugins/Maya/Common/rendererDesc".format(redshift_root)
    env.REDSHIFT_CUSTOM_TEMPLATE_PATH = r"{}/Plugins/Maya/Common/scripts/NETemplates".format(redshift_root)
    env.REDSHIFT_MAYAEXTENSIONSPATH = r"{}/Plugins/Maya/{}/nt-x86-64/extensions".format(redshift_root, maya_version)
    env.REDSHIFT_PROCEDURALSPATH = r"{}/Procedurals".format(redshift_root)

    env.PATH.append(r"{}/bin".format(redshift_root))
    env.MAYA_PLUG_IN_PATH.append(r"{}/Plugins/Maya/{}/nt-x86-64".format(redshift_root, maya_version))
    env.MAYA_SCRIPT_PATH.append(r"{}/Plugins/Maya/Common/scripts".format(redshift_root))
    env.PYTHONPATH.append(r"{}/Plugins/Maya/Common/scripts".format(redshift_root))
    env.XBMLANGPATH.append(r"{}/Plugins/Maya/Common/icons".format(redshift_root))
    env.MAYA_RENDER_DESC_PATH.append(r"{}/Plugins/Maya/Common/rendererDesc".format(redshift_root))
    env.MAYA_CUSTOM_TEMPLATE_PATH.append(r"{}/Plugins/Maya/Common/scripts/NETemplates".format(redshift_root))
