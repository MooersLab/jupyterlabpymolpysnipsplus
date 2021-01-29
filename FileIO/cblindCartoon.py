# Description:  Color cartoon with colorblind friendly colors. Requires that the pymolshortcuts.py file is loaded. This has been applied to PDB-ID 7JU6. The protein is human RET kinase, and the drug is selpercatinib, a FDA approved drug for treating several cancers.
# Source:  placeHolder

"""
cmd.do('CB;')
cmd.do('color cb_lightblue, ss h;')
cmd.do('color cb_vermillion, ss s;')
cmd.do('color lightorange, ss l+"";')
"""

cmd.do('CB;')
cmd.do('color cb_lightblue, ss h;')
cmd.do('color cb_vermillion, ss s;')
cmd.do('color lightorange, ss l+"";')
