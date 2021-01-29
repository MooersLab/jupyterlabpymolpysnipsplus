# Description:  Examples of a triple water pentagon. Zoom in on the selection. Edit by changing the residue number.
# Source:  placeHolder

"""
cmd.do('fetch ${1:lw9}, async=0; ')
cmd.do('zoom resi ${2:313}; ')
cmd.do('preset.technical(selection="all", mode=1);')
"""

cmd.do('fetch lw9, async=0; ')
cmd.do('zoom resi 313; ')
cmd.do('preset.technical(selection="all", mode=1);')
