# An example of a package referencing something from outside
# of the local package.
import os

name = "redshift_core"
version = "3.0.45"

authors = ['Redshift']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

description = """
Redshift is an award-winning, production ready GPU renderer for fast 3D rendering"""


def commands():
    global env

    env.REDSHIFT_COREDATAPATH = "{root}/resources"
    env.redshift_LICENSE = "5053@192.168.3.207" # 3d sparrow. VPN needs to be on
