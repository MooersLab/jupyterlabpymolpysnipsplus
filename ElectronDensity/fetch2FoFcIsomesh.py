# Description:  Fetch 2FoFc map as an isomesh.
# Source:  placeHolder

"""
cmd.do('fetch ${1:3nd4}, ${1:3nd4}_2fofc, type=2fofc, async=0;')
cmd.do('isomesh 2fofcmap, ${1:3nd4}_2fofc, 1, ${1:3nd4}, carve = 1.8;')
"""

cmd.do('fetch 3nd4, 3nd4_2fofc, type=2fofc, async=0;')
cmd.do('isomesh 2fofcmap, 3nd4_2fofc, 1, 3nd4, carve = 1.8;')
