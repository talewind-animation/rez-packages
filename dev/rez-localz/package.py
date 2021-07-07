name = "localz"
version = "0.4.2"
requires = ["python-2.7+,<4", "bleeding_rez-2.29+"]
build_command = "python {root}/install.py"


def commands():
    global env

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
