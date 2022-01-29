# An example of a package referencing something from outside
# of the local package.

name = "sublime"
version = "4.1.3"
requires = [
    "python",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1.3.1+"]

def commands():

    global env
    global alias

    sublime_root = "C:\\Program Files\\Sublime Text"

    env["PATH"].append(sublime_root)
