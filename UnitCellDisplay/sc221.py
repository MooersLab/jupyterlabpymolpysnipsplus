# Description:  Display all symmetry mates in 2 x 2 x 1 array of unit cells. Uses supercell.py in $HOME/Scripts/PyMOLscripts/.
# Source:  placeHolder

"""
cmd.do('run $HOME/${1:Scripts/PyMOLscripts/}supercell.py;')
cmd.do('supercell 2, 2, 1, ,  ${2:orange},  ${3:supercell1}, 1;')
"""

cmd.do('run $HOME/Scripts/PyMOLscripts/supercell.py;')
cmd.do('supercell 2, 2, 1, ,  orange,  supercell1, 1;')
