# An example of a package referencing something from outside
# of the local package.

name = "katana"
version = "5.0.1"

requires = [
    "rlm",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

def commands():
    import os

    global this
    global env
    global alias

    major, bld = str(this.version).rsplit(".", 1)
    version = "{}v{}".format(major, bld)
    env["KATANA_VERSION"] = version

    # Edit these to support more versions of Maya
    if os.name == "nt":
        katana_root = "C:\\Program Files\\Katana{}".format(version)
        bindir = os.path.join(katana_root, "bin")
        ext = ".exe"

    if os.path.exists(katana_root):
        env.KATANA_ROOT=katana_root
        env.PATH.append(bindir)

        # Make the example projects like the PyMock asset plugins available in KATANA
        env.KATANA_RESOURCES.append("{}\\plugins\\Resources\\Examples".format(katana_root))

        env.KATANA_TAGLINE="Katana Vanilla"

        fname = os.path.join(bindir, "katanaBin" + ext)
        fname = fname.replace(" ", "` ")  # Escape spaces for PowerShell
        alias("katana", fname)

