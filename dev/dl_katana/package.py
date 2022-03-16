# An example of a package referencing something from outside
# of the local package.
name = "dl_katana"
version = "1.1.1"

authors = ['3Delight']

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1",]

requires = [
    "~katana-5.0",
]

plugin_for = ["katana"]

def commands():
    global env

    env.DELIGHT = "{root}/resources"
    env.PATH.append("{root}/resources/bin")
    env.KATANA_RESOURCES.append("{root}/resources/3DelightForKatana")


    env.KATANA_TAGLINE= env.KATANA_TAGLINE.value() + "\nrenderer 3Delight"
    env.DEFAULT_RENDERER="arnold"
