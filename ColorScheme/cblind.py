# Description:  Apply color blind friendly to ribbon diagrams. Edit the path to the Pymol-script-repo in your computer account. See PyMOL wiki for more information about the Pymol-script-reo.
# Source:  placeHolder

"""
cmd.do('run ~/${1:Pymol-script-repo}/colorblindfriendly.py;')
cmd.do('as cartoon;')
cmd.do('color cb_red, ss H;')
cmd.do('color cb_yellow,ss S;')
cmd.do('color cb_green, ss L+;')
"""

cmd.do('run ~/Pymol-script-repo/colorblindfriendly.py;')
cmd.do('as cartoon;')
cmd.do('color cb_red, ss H;')
cmd.do('color cb_yellow,ss S;')
cmd.do('color cb_green, ss L+;')
