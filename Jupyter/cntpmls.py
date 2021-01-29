# Description:  Count number of *.pml files in current directory.
# Source:  placeHolder

"""
cmd.do('print("Count the number of pml (Pymol macro language) files in current directory.");')
cmd.do('print("Usage: cntpmls");')
cmd.do('myPath = os.getcwd();')
cmd.do('pmlCounter = len(glob.glob1(myPath,"*.pml"));')
cmd.do('print("Number of pml files in the current directory: ", pmlCounter);')
"""

cmd.do('print("Count the number of pml (Pymol macro language) files in current directory.");')
cmd.do('print("Usage: cntpmls");')
cmd.do('myPath = os.getcwd();')
cmd.do('pmlCounter = len(glob.glob1(myPath,"*.pml"));')
cmd.do('print("Number of pml files in the current directory: ", pmlCounter);')
