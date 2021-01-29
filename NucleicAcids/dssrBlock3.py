# Description:  DSSR block representation for a multi-state example after loading the dssr_block.py script by Thomas Holder. The x3dna-dssr executable needs to be in the PATH. Edit the path to Thomas Holder's block script.
# Source:  Generated while helping Miranda Adams at U of Saint Louis.

"""
cmd.do('reinitialize;')
cmd.do('run ${1:"/Users/blaine/.pymol/startup/dssr_block.py"};')
cmd.do('fetch ${2:2n2d}, async=0;')
cmd.do('dssr_block  ${2:2n2d}, 0;')
cmd.do('set all_states;')
"""

cmd.do('reinitialize;')
cmd.do('run "/Users/blaine/.pymol/startup/dssr_block.py";')
cmd.do('fetch 2n2d, async=0;')
cmd.do('dssr_block  2n2d, 0;')
cmd.do('set all_states;')
