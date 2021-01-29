# Description:  Coloring two strand differently of a double helix makes it easier to for the viewer to distinguish the two strands. The set command has the syntax of setting_name [, setting_value [, selection [,state ]]] . In this case, the selection has to be global, object, object-state, or per-atom settings. It cannot be a named selection. This is a weak spot in PyMOL. Coloring two strand differently of a double helix makes it easier to for the viewer to distinguish the two strands. Many double-stranded helices have one strand in the asymmetric unit. The second strand is in the biological unit. The coordinates for the second strand are in the pdb1 file type at the PDB. The second strand is in the second state, which is equivalent to the second model in the pdb file. The strands are labeled chain A and B (via the cartoon_nucliec_acid_color setting). The bases are colored differently too (via the cartoon_ladder_color setting).
# Source:  Generated while helping Miranda Adams at U of Saint Louis.

"""
cmd.do('fetch ${1:3nd3}, ${2:3nd3}, type=${3:pdb1};')
cmd.do('set all_states, on;')
cmd.do('create chA, ${2:3nd3}, 1, 1;')
cmd.do('create chB, ${2:3nd3}, 2, 1;')
cmd.do('# colors only the backbone;')
cmd.do('set cartoon_nucleic_acid_color, ${4:magenta}, chA;')
cmd.do('set cartoon_nucleic_acid_color, ${5:orange}, chB;')
cmd.do('# color the bases;')
cmd.do('set cartoon_ladder_color,  ${6:density}, chA;')
cmd.do('set cartoon_ladder_color,  ${7:yellow}, chB;')
"""

cmd.do('fetch 3nd3, 3nd3, type=pdb1;')
cmd.do('set all_states, on;')
cmd.do('create chA, 3nd3, 1, 1;')
cmd.do('create chB, 3nd3, 2, 1;')
cmd.do('# colors only the backbone;')
cmd.do('set cartoon_nucleic_acid_color, magenta, chA;')
cmd.do('set cartoon_nucleic_acid_color, orange, chB;')
cmd.do('# color the bases;')
cmd.do('set cartoon_ladder_color,  density, chA;')
cmd.do('set cartoon_ladder_color,  yellow, chB;')
