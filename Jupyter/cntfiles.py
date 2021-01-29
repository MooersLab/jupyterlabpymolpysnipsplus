# Description:  Count number of files in current directory.
# Source:  placeHolder

"""
cmd.do('print("Count the files in the directory.")')
cmd.do('print("Usage: cntfiles.")')
cmd.do('# simple version for working with CWD')
cmd.do('print("Number of files in current working directory: ", len([name for name in os.listdir(".") if os.path.isfile(name)]))')
"""

cmd.do('print("Count the files in the directory.")')
cmd.do('print("Usage: cntfiles.")')
cmd.do('# simple version for working with CWD')
cmd.do('print("Number of files in current working directory: ", len([name for name in os.listdir(".") if os.path.isfile(name)]))')
