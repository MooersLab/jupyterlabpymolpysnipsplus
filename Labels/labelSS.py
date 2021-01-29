# Description:  Label SS.
# Source:  placeHolder

"""
cmd.do('alter ${1:chain A}, ss="${2:helix}";')
cmd.do('label (%2),"%3";')
"""

cmd.do('alter chain A, ss="helix";')
cmd.do('label (%2),"%3";')
