# Description:  Count number of *.pse files in current directory.
# Source:  placeHolder

"""
cmd.do('print("Count the number of *.pse (session) files in current directory.");')
cmd.do('print("Usage: cntpses");')
cmd.do('myPath = os.getcwd();')
cmd.do('pseCounter = len(glob.glob1(myPath,"*.pse"));')
cmd.do('print("Number of *.pse (session) files in the current directory: ", pseCounter);')
"""

cmd.do('print("Count the number of *.pse (session) files in current directory.");')
cmd.do('print("Usage: cntpses");')
cmd.do('myPath = os.getcwd();')
cmd.do('pseCounter = len(glob.glob1(myPath,"*.pse"));')
cmd.do('print("Number of *.pse (session) files in the current directory: ", pseCounter);')
