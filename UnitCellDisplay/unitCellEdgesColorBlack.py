# Description:  Color unit cell edges black. The settings for controlling the unit cell color are hard to find.
# Source:  placeHolder

"""
cmd.do('# show the unit cell;')
cmd.do('show cell;')
cmd.do('color black, ${1:1lw9};')
cmd.do('# color by atom with carbons colored green,')
cmd.do('util.${2:cbag};')
cmd.do('set cgo_line_width, 2.5;')
cmd.do('png  ${3:testCell3}.png, ${4:1600},${5:1600};${6:600};${7:0}')
"""

cmd.do('# show the unit cell;')
cmd.do('show cell;')
cmd.do('color black, 1lw9;')
cmd.do('# color by atom with carbons colored green,')
cmd.do('util.cbag;')
cmd.do('set cgo_line_width, 2.5;')
cmd.do('png  testCell3.png, 1600,1600;600;0')
