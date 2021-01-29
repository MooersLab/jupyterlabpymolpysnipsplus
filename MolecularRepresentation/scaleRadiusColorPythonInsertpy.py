# Description:  Python block insert for scaleRadiusColorpy.
# Source:  placeHolder

"""
cmd.do('# scale the b−values;')
cmd.do('M = max(stored.bb);')
cmd.do('scaledBB = map(lambda x: float (x/M), stored.bb);')
cmd.do('count = 0;')
cmd.do('# set the sphere radii independently;')
cmd.do('#[(cmd.set("sphere_scale", x ,"ID %s"%count); count = count + 1) for x in scaledBB]')
cmd.do('for x in scaledBB:')
cmd.do('  cmd.set("sphere_scale", x ,"ID %s"%count)')
cmd.do('  count = count + 1')
"""

cmd.do('# scale the b−values;')
cmd.do('M = max(stored.bb);')
cmd.do('scaledBB = map(lambda x: float (x/M), stored.bb);')
cmd.do('count = 0;')
cmd.do('# set the sphere radii independently;')
cmd.do('#[(cmd.set("sphere_scale", x ,"ID %s"%count); count = count + 1) for x in scaledBB]')
cmd.do('for x in scaledBB:')
cmd.do('  cmd.set("sphere_scale", x ,"ID %s"%count)')
cmd.do('  count = count + 1')
