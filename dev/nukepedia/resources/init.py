import nuke

# nkplugins
nuke.pluginAddPath("./nkPlugins/pgBokeh{}".format(nuke.NUKE_VERSION_MAJOR))
if int(nuke.NUKE_VERSION_MAJOR) < 13:
    nuke.pluginAddPath("./nkPlugins/cryptomatte")
    import cryptomatte_utilities
    cryptomatte_utilities.setup_cryptomatte()

# nukepedia
nuke.pluginAddPath("./nukepedia/python")
nuke.pluginAddPath("./nukepedia/gizmos")
nuke.pluginAddPath("./nukepedia/icons")
nuke.pluginAddPath("./nukepedia/w_hotbox")
