# Description:  Print the atom number2 of a residue.
# Source:  https://www.pymolwiki.org/index.php/Sync

"""
cmd.do('iterate (resi ${1:1}), print(name + " %i${1:5}" % ID);')
"""

cmd.do('iterate (resi 1), print(name + " %i5" % ID);')
