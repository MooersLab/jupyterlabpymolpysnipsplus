# Description:  Fetch 2FoFc map as an isosurface. Edit the PDB-ID code. Use lowercase letter for the fifth character to select a single chain.
# Source:  placeHolder

"""
cmd.do('fetch ${1:3nd4}, ${1:3nd4}_2fofc, type=2fofc, async=0;')
cmd.do('# Render and display a contour of this map as a chicken wire representation.;')
cmd.do('isosurface 2fofcmap, ${1:3nd4}_2fofc, 1, ${1:3nd4}, carve = 1.8;')
"""

cmd.do('fetch 3nd4, 3nd4_2fofc, type=2fofc, async=0;')
cmd.do('# Render and display a contour of this map as a chicken wire representation.;')
cmd.do('isosurface 2fofcmap, 3nd4_2fofc, 1, 3nd4, carve = 1.8;')
