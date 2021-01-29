# Description:  Count number of *.mtz files in current directory.
# Source:  placeHolder

"""
cmd.do('print("Count the number of mtz structure factor files in current directory.");')
cmd.do('print("Usage: cntmtzs");')
cmd.do('myPath = os.getcwd();')
cmd.do('mtzCounter = len(glob.glob1(myPath,"*.mtz"));')
cmd.do('print("Number of number of mtz structure factor  files in the current directory: ", mtzCounter);')
"""

cmd.do('print("Count the number of mtz structure factor files in current directory.");')
cmd.do('print("Usage: cntmtzs");')
cmd.do('myPath = os.getcwd();')
cmd.do('mtzCounter = len(glob.glob1(myPath,"*.mtz"));')
cmd.do('print("Number of number of mtz structure factor  files in the current directory: ", mtzCounter);')
