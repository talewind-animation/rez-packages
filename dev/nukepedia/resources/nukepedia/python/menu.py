# imports
import os

import nuke
import nukescripts
import W_hotbox
import W_hotboxManager
import W_smartAlign

#############################NUKEPEDIA#############################
toolbar = nuke.toolbar("Nodes")
k = toolbar.addMenu("NukePedia")
k.addCommand('Multilabeler', 'nuke.createNode("Multilabeler")')
k.addCommand("DespillMadness", "nuke.createNode(\"DespillMadness\")")
k.addCommand("RealChroma", "nuke.createNode(\"RealChroma\")")
k.addCommand("RealHeatDistort", "nuke.createNode(\"RealHeatDistort\")")
k.addCommand("Luma_Grain", "nuke.createNode(\"L_Grain_v05\")")
k.addCommand("Luma_Fuse", "nuke.createNode(\"L_Fuse_v06\")")
k.addCommand("P_Matte", "nuke.createNode(\"P_Matte\")")
k.addCommand("P_Ramp", "nuke.createNode(\"P_Ramp\")")
k.addCommand("EdgeExtend2", "nuke.createNode(\"EdgeExtend2\")")
k.addCommand("expoglow", "nuke.createNode(\"expoglow\")")
k.addCommand("X_Aton", "nuke.createNode(\"X_Aton\")")
k.addCommand("Vignette", "nuke.createNode(\"dg_Vignette\")")
k.addCommand("Shuffle AOV's", "shuffleAOVs()" )

#############################SHUFFLE_AOV's#############################

def  shuffleAOVs(hide_input=True):
    blacklist = [
        'cryptomatte00',
        'cryptomatte01',
        'cryptomatte02',
        'cryptomatte03',
        'rgba',
        'rgb',
        'alpha',
        'cryptomatte',
        'other',
    ]

    node = nuke.selectedNode()
    layers = list(set([c.split('.')[0] for c in node.channels() if not c.split('.')[0] in blacklist]))

    for layer in layers:
        shuffle = nuke.nodes.Shuffle()
        shuffle['label'].setValue(
            '<font size=6 color="orange">{}</font>'.format(layer)+
            '\n<font size = 5 color="cyan">[value in]</font>'
        )
        shuffle['in'].setValue(layer)
        shuffle['hide_input'].setValue(hide_input)
        shuffle['tile_color'].setValue(858993663)
        shuffle.setInput(0, node)
#############################SMART_ALIGN#############################

import W_smartAlign

menuBar = nuke.menu("Nuke")
menuBar.addCommand("Edit/Node/Align/Left", 'W_smartAlign.alignNodes("left")', "Alt+left", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Right", 'W_smartAlign.alignNodes("right")', "Alt+right", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Up", 'W_smartAlign.alignNodes("up")', "Alt+up", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Down", 'W_smartAlign.alignNodes("down")', "Alt+down", shortcutContext=2)
