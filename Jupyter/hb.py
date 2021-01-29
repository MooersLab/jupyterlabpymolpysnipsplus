# Description:  Creates an object of all H-bonds found by PyMOL.
# Source:  placeHolder

"""
cmd.do('cmd.distance("hbonds", "all", "all", "3.2", mode="2")')
cmd.do('cmd.set("dash_gap","0.4")')
cmd.do('cmd.set("dash_color","grey30")')
cmd.do('cmd.set("dash_width","1.5")')
cmd.do('cmd.set("dash_length",".25")')
cmd.do('print("Enter 'rmhb' to remove the hbonds.")')
"""

cmd.do('cmd.distance("hbonds", "all", "all", "3.2", mode="2")')
cmd.do('cmd.set("dash_gap","0.4")')
cmd.do('cmd.set("dash_color","grey30")')
cmd.do('cmd.set("dash_width","1.5")')
cmd.do('cmd.set("dash_length",".25")')
cmd.do('print("Enter 'rmhb' to remove the hbonds.")')
