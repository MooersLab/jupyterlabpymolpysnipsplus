# Description:  Print the B-factors of a residue.
# Source:  placeHolder

"""
cmd.do('remove element h; iterate resi ${1: 1:13}, print(resi, name,b);')
"""

cmd.do('remove element h; iterate resi  1:13, print(resi, name,b);')
