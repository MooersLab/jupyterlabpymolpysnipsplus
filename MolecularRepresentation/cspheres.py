"""
cmd.do('as spheres;')
cmd.do('color gray30, chain ${1:A};')
cmd.do('color white, chain ${2:B};')
cmd.do('color green, name CL;')
cmd.do('color brown, resn NAG;')
cmd.do('color red, resi 381;')
cmd.do('remove solvent;')
cmd.do('unset specular;')
cmd.do('set ray_trace_gain, 0;')
cmd.do('set ray_trace_mode, 3;')
cmd.do('bg_color white;')
cmd.do('set ray_trace_color, black;')
cmd.do('unset depth_cue;')
"""
cmd.do('as spheres;')
cmd.do('color gray30, chain A;')
cmd.do('color white, chain B;')
cmd.do('color green, name CL;')
cmd.do('color brown, resn NAG;')
cmd.do('color red, resi 381;')
cmd.do('remove solvent;')
cmd.do('unset specular;')
cmd.do('set ray_trace_gain, 0;')
cmd.do('set ray_trace_mode, 3;')
cmd.do('bg_color white;')
cmd.do('set ray_trace_color, black;')
cmd.do('unset depth_cue;')

# Description:  Colored spheres.
# Source:  placeHolder

