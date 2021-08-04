name = "code"
version = "1.58.2"
requires = []

authors = ['Microsoft']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

description = """
Visual Studio Code is a source-code editor made by Microsoft."""


def commands():
    from os.path import expanduser
    home = expanduser("~")

    global env

    env.PATH.append(home+"\\AppData\\Local\\Programs\\Microsoft VS Code")