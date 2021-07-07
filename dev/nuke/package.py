# An example of a package referencing something from outside
# of the local package.

name = "nuke"
version = "11.3.5"
requires = [
    "quicktime",
    "rlm",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1.3.1+"]

# Cross-platform binaries (i.e. shell scripts)
# are built and deployed with this package.
tools = [
    "nuke",
]

_data = {
    "label": "Foundry Nuke",
    "color": "#251",
    "icon": "{root}/resources/icon_256x256.png",
}


def commands():
    import os
    global env
    global alias
    global system



    version, version_dev = str(this.version).rsplit(".", 1)
    version_name = "{}v{}".format(version, version_dev)

    executable = "Nuke{}".format(version)

    if system.platform == "windows":
        bindir = "C:\\Program Files\\Nuke{}".format(version_name)
        ext = ".exe"

    elif system.platform == "linux":
        bindir = "/opt/nuke{}/bin/".format(version_name)

    if os.path.exists(bindir):
        fname = os.path.join(bindir, executable + ext)
        fname = fname.replace(" ", "` ")  # Escape spaces for PowerShell
        alias("nuke", fname)
        alias("nukex", "{} --nukex".format(fname))
        alias("nukestudio", "{} --studio".format(fname))
        alias("hiero", "{}  --hiero".format(fname))
    else:
        print("WARNING: Missing files: %s" % bindir)

    # bindir = "\"%s\"" % bindir

    env["PATH"].append(bindir)
