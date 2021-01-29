# Description:  Display the bond valence of ligands only.
# Source:  https://www.mail-archive.com/pymol-users@lists.sourceforge.net/msg15668.html

"""
cmd.do('set valence, on, resn ${1:RZS}; set valence, off, not resn ${2:RZS};')
"""

cmd.do('set valence, on, resn RZS; set valence, off, not resn RZS;')
