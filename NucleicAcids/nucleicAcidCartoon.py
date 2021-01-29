# Description:  Settings for nucliec acid cartoon. The dark blue used for electron density maps is called `density`. The cartoon_ladder_radius should be renamed the cartoon_rung_radius. The dimensions are in Angstroms.
# Source:  Generated while helping Miranda Adams at U of Saint Louis.

"""
cmd.do('set cartoon_ladder_radius, ${2:0.2};')
cmd.do('set cartoon_nucleic_acid_color, ${3:red};')
cmd.do('# The cartoon ring modes range from 0 to 4.;')
cmd.do('set cartoon_ring_mode, ${4:2};')
"""

cmd.do('set cartoon_ladder_radius, 0.2;')
cmd.do('set cartoon_nucleic_acid_color, red;')
cmd.do('# The cartoon ring modes range from 0 to 4.;')
cmd.do('set cartoon_ring_mode, 2;')
