"""
cmd.do('fetch ${1:3nd3},name=${1:3nd3}, type=pdb, async=0')
cmd.do('hide (name H*);')
cmd.do('hide lines;')
cmd.do('show sticks;')
cmd.do('set stick_radius, ${2:1.2};')
cmd.do('set nb_sphere_radius, ${3:0.35};')
cmd.do('orient;')
"""
cmd.do('fetch 3nd3,name=3nd3, type=pdb, async=0')
cmd.do('hide (name H*);')
cmd.do('hide lines;')
cmd.do('show sticks;')
cmd.do('set stick_radius, 1.2;')
cmd.do('set nb_sphere_radius, 0.35;')
cmd.do('orient;')

# Description:  Load PDB ball-and-stick.
# Source:  placeHolder

