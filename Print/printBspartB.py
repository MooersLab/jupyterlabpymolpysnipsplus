# Description:  Print B factors of part B of a residue.
# Source:  placeHolder

"""
cmd.do('iterate resi ${1:38} and altloc ${2:B}, print resi, name, alt, b;')
"""

cmd.do('iterate resi 38 and altloc B, print resi, name, alt, b;')
