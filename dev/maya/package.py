# An example of a package referencing something from outside
# of the local package.

name = "maya"
version = "2022.0.1"
requires = [
        "quicktime",
    ]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

# Cross-platform binaries (i.e. shell scripts)
# are built and deployed with this package.
tools = [
    "maya",
    "mayapy",
    "render",
    "mayabatch",
]

def commands():
    import os

    global this
    global env
    global alias
    global system

    # Some basic Maya hygene
    env["MAYA_DEBUG_ENABLE_CRASH_REPORTING"] = "0"
    env["MAYA_DISABLE_CLIC_IPM"] = "Yes"  # Disable the AdSSO process
    env["MAYA_DISABLE_CIP"] = "Yes"       # Shorten time to boot
    env["MAYA_DISABLE_CER"] = "Yes"
    env["PYMEL_SKIP_MEL_INIT"] = "Yes"
    env["LC_ALL"] = "C"                   # Mute color management warnings

    exes = ["maya", "mayapy", "mayabatch", "render"]
    ext = ""
    version = str(this.version).split(".", 1)[0]
    env["MAYA_VERSION"] = version

    # Edit these to support more versions of Maya
    if os.name == "nt":
        bindir = r"c:\program files\autodesk\maya{}\bin".format(version)
        ext = ".exe"

    if os.path.exists(bindir):
        env.PATH.append(bindir)
        for exe in exes:
            fname = os.path.join(bindir, exe + ext)
            fname = fname.replace(" ", "` ")  # Escape spaces for PowerShell
            alias(exe, fname)
    else:
        if system.platform == "windows":
            alias("maya", "notepad {root}/resources/readme.txt")
        else:
            # Making some assumptions here
            # TODO: Bullet proof this
            alias("maya", "gedit {root}/resources/readme.txt")
