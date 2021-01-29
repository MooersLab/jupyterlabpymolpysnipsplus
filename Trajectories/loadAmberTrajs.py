# Description:  The amber trajectories have to be loaded into the same object.
# Source:  https://www.mail-archive.com/pymol-users@lists.sourceforge.net/msg15508.html

"""
cmd.do('load ${1:file}.top, ${2:protein};')
cmd.do('load ${1:file}.rst, ${2:protein};')
"""

cmd.do('load file.top, protein;')
cmd.do('load file.rst, protein;')
