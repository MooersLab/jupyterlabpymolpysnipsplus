# Description:  Display the famous Asp70-His31 salt-bridge from T4 lysozyme that contributes3-5 kcal/mol to protein stability. 
# Source:  placeHolder

"""
cmd.do('fetch ${1:1lw9}, async=0; ')
cmd.do('zoom (${2:resi 31 or resi 70}); ')
cmd.do('preset.technical(selection='all'); ')
cmd.do('bg_color ${3:gray70}; ')
cmd.do('clip slab, 7,(${4:resi 31 or resi 70});')
cmd.do('rock;')
"""

cmd.do('fetch 1lw9, async=0; ')
cmd.do('zoom (resi 31 or resi 70); ')
cmd.do('preset.technical(selection='all'); ')
cmd.do('bg_color gray70; ')
cmd.do('clip slab, 7,(resi 31 or resi 70);')
cmd.do('rock;')
