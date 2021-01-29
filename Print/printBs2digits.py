# Description:  Print B--factors for a residue with the B-factors rounded off to two decimal places.
# Source:  placeHolder

"""
cmd.do('iterate (resi ${1:133}), print(name + " %.2f" % b);')
"""

cmd.do('iterate (resi 133), print(name + " %.2f" % b);')
