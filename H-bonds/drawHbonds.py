# Description:  Display H-bonds as dashes colored black.
# Source:  placeHolder

"""
cmd.do('hide everything, hydrogens;')
cmd.do('hide labels;')
cmd.do('# set the color of the dashed lines representing the H-bond.;')
cmd.do('set dash_color, ${1:black};')
cmd.do('set dash_gap, 0.4;')
cmd.do('set dash_radius, 0.08;')
"""

cmd.do('hide everything, hydrogens;')
cmd.do('hide labels;')
cmd.do('# set the color of the dashed lines representing the H-bond.;')
cmd.do('set dash_color, black;')
cmd.do('set dash_gap, 0.4;')
cmd.do('set dash_radius, 0.08;')
