name = "rlm"
version = "1.0.0"

build_command = False

def commands():
    global env

    license_server = "5053@localhost"

    env.RLM_LICENSE = r"C:\Program Files\rlm"
    env.foundry_LICENSE = license_server
    env.peregrinel_LICENSE = license_server
    env.solidangle_LICENSE = license_server
    env.foundry_LICENSE = license_server
