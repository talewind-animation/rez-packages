# An example of a package referencing something from outside
# of the local package.
name = "deadlineapi"
version = "10.0.25"

authors = ['Thinkbox']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

description = """
Deadline python api"""

def commands():
    global env

    env.PYTHONPATH.append("{root}/resources")
