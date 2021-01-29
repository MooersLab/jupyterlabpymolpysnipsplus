# Description:  Display all symmetry mates in a 4 x 1 x 4 array. Uses supercell.py in $HOME/Scripts/PyMOLscripts/.
# Source:  placeHolder

"""
cmd.do('run $HOME/${1:Scripts/PyMOLscripts/}supercell.py;')
cmd.do('supercell 4, 1, 4, ,  ${2:orange},  ${3:supercell1}, 1;')
"""

cmd.do('run $HOME/Scripts/PyMOLscripts/supercell.py;')
cmd.do('supercell 4, 1, 4, ,  orange,  supercell1, 1;')
