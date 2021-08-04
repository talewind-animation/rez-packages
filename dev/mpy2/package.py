name = "mpy2"
version = "1.0.0"

description = """Load maya with Python 2"""

build_command = False

requires = [
    "maya>=2022",
]

def commands():
    global env

    env["MAYA_PYTHON_VERSION"] = 2
