# Description:  Center pi. Edit the atoms selected for positioning the pseudoatom.
# Source:  placeHolder

"""
cmd.do('pseudoatom pi_cent,/${1:3nd3}/${2:A}/${3:U`15}/cg+cz;')
cmd.do('dist pi_cent////ps1, b/${4:U`15}/${5:aaa};')
"""

cmd.do('pseudoatom pi_cent,/3nd3/A/U`15/cg+cz;')
cmd.do('dist pi_cent////ps1, b/U`15/aaa;')
