# Description:  Imports needed for most uses of pymol in Jupyter. Combination of importPyMOL and importPythonDisplay.
# Source:  placeHolder

"""
cmd.do('from pymol import cmd')
cmd.do('from IPython.display import Image')
cmd.do('PATH = "${1:/Users/blaine/}"')
cmd.do('cmd.do("run ${2:/Users/blaine/Scripts/PyMOLScripts/pymolshortcuts.py")')
"""

cmd.do('from pymol import cmd')
cmd.do('from IPython.display import Image')
cmd.do('PATH = "/Users/blaine/"')
cmd.do('cmd.do("run /Users/blaine/Scripts/PyMOLScripts/pymolshortcuts.py")')
