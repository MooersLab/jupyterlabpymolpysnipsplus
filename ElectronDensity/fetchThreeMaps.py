# Description:  Display three electron density maps as isomesh.
# Source:  placeHolder

"""
cmd.do('fetch ${1:4dgr}, type=pdb;')
cmd.do('# Make sure to rename map file so that ;')
cmd.do('# the root filename differs from pdb root filename;')
cmd.do('fetch ${1:4dgr},  ${1:4dgr}_2fofc, type=2fofc;')
cmd.do('fetch ${1:4dgr}, ${1:4dgr}_fofc, type=fofc;')
cmd.do('select  ${2:glycan}, ${3:resid 200 or resid 469:477};')
cmd.do('isomesh ${4:mesh1}, 2fofc, 1.0, ${2:glycan};')
cmd.do('color density, ${4:mesh1};')
cmd.do('isomesh ${5:mesh2}, fofc, 3.0, ${2:glycan};')
cmd.do('color green, ${5:mesh2};')
cmd.do('isomesh ${6:mesh3}, fofc, -3.0, ${2:glycan};')
cmd.do('color red, ${6:mesh3};')
"""

cmd.do('fetch 4dgr, type=pdb;')
cmd.do('# Make sure to rename map file so that ;')
cmd.do('# the root filename differs from pdb root filename;')
cmd.do('fetch 4dgr,  4dgr_2fofc, type=2fofc;')
cmd.do('fetch 4dgr, 4dgr_fofc, type=fofc;')
cmd.do('select  glycan, resid 200 or resid 469:477;')
cmd.do('isomesh mesh1, 2fofc, 1.0, glycan;')
cmd.do('color density, mesh1;')
cmd.do('isomesh mesh2, fofc, 3.0, glycan;')
cmd.do('color green, mesh2;')
cmd.do('isomesh mesh3, fofc, -3.0, glycan;')
cmd.do('color red, mesh3;')
