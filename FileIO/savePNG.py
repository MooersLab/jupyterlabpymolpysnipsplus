# Description:  # Save a png file of current scene to the current directory. PyMOL writes out only png files. This file may need to be converted to a tiff file. See the png2tiff snippet for a bash script that converts all png files in a folder into tiff files.
# 1: png filename
# 2: x-dimension in pixels
# 3: y-dimension in pixels, 1600 x 1000 approximates the golden ratio. Usually want a square for multipanel figures.
# 4: dots per inch, 
# 5: ray tracing off, 0; ray tracing on, 1
# should also consider image without ray tracing shadows. 
# Source:  placeHolder

"""
cmd.do('png ${1:saveMe}.png, ${2:1920}, ${3:1920}, ${4:600}, ${5:1};')
"""

cmd.do('png saveMe.png, 1920, 1920, 600, 1;')
