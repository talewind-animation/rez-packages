# An example of a package referencing something from outside
# of the local package.

name = "houdini"
version = "18.5.499"
requires = []

authors = ['SideFX']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

description = """
Houdini is a 3D animation software application developed by Toronto-based SideFX."""


def commands():
    import os

    global this
    global env
    global alias

    env.HOUDINI_VERSION = this.version
    env.HOUDINI_TEXT_CONSOLE = 1
    env.HOUDINI_ACCESS_METHOD = 2 # ignore the user and group permissions
    env.HOUDINI_VERSION = this.version
    env.HOUDINI_PATH = "&"

    exes = [
            {"app": "houdinifx", "alias": "houdini"},
            {"app": "pilotpdg", "alias": "pdg"},
            {"app": "mplay", "alias": "mplay"},
            {"app": "gplay", "alias": "gplay"},
        ]
    ext = ""

    # Edit these to support more versions of Maya
    if os.name == "nt":
        bindir = r"C:\Program Files\Side Effects Software\Houdini {}\bin".format(version)
        ext = ".exe"


    if os.path.exists(bindir):
        env.PATH.prepend(bindir)
        for exe in exes:
            fname = os.path.join(bindir, exe["app"] + ext)
            fname = fname.replace(" ", "` ")  # Escape spaces for PowerShell
            alias(exe["alias"], fname)
    else:
        print("Houdini install directory not found!")
