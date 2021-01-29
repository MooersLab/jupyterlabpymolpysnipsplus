# Description:  Run supercell script to generate three cells in all directions. This script was written by Thomas Holder.
# Source:  placeHolder

"""
cmd.do('run $HOME/${1:Scripts/PyMOLscripts/}supercell.py;')
cmd.do('supercell 2, 2, 2, , ${2:orange},  ${3:supercell1}, 1;')
"""

cmd.do('run $HOME/Scripts/PyMOLscripts/supercell.py;')
cmd.do('supercell 2, 2, 2, , orange,  supercell1, 1;')
