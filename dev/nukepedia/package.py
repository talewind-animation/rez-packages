name = "nukepedia"
version = "1.0.0"


build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "~nuke>=8",
]

_environ = {
    "OFX_PLUGIN_PATH": "{root}/resources/OFX",
    "W_HOTBOX_REPO_PATHS": "{root}/resources/nukepedia/w_hotbox/hotbox",
    "W_HOTBOX_REPO_NAMES": "default",
    "W_HOTBOX_ICON_LOC": "{root}/resources/nukepedia/w_hotbox/icons/W_hotbox",
    "W_HOTBOX_HIDE_ICON_LOC": "1",
    "NUKE_PATH": [
        "{root}/resources",
    ],
}


def commands():
    global env
    global this
    global expandvars

    _environ = this._environ

    for key, value in _environ.items():
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)
