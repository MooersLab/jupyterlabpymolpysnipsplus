# Description:  Count number of *.ccp4 (electron density map) files in current directory.
# Source:  placeHolder

"""
cmd.do('print("Count the number of ccp4 electron density files in current directory.");')
cmd.do('print("Usage: cntccp4s");')
cmd.do('myPath = os.getcwd();')
cmd.do('ccp4Counter = len(glob.glob1(myPath,"*.pse"));')
cmd.do('print("Number of number of ccp4 electron density files in the current directory: ", ccp4Counter);')
"""

cmd.do('print("Count the number of ccp4 electron density files in current directory.");')
cmd.do('print("Usage: cntccp4s");')
cmd.do('myPath = os.getcwd();')
cmd.do('ccp4Counter = len(glob.glob1(myPath,"*.pse"));')
cmd.do('print("Number of number of ccp4 electron density files in the current directory: ", ccp4Counter);')
