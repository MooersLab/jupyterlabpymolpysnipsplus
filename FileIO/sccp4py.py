# Description:  Save electron density map flle with timestamp.
# Source:  placeHolder

"""
cmd.do('import datetime;')
cmd.do('from pymol import cmd; ')
cmd.do('DT =datetime.datetime.now().strftime("yr%Ymo%mday%dhr%Hmin%M");')
cmd.do('s = str(DT); ')
cmd.do('cmd.save(stemName+s+".ccp4"); ')
"""

cmd.do('import datetime;')
cmd.do('from pymol import cmd; ')
cmd.do('DT =datetime.datetime.now().strftime("yr%Ymo%mday%dhr%Hmin%M");')
cmd.do('s = str(DT); ')
cmd.do('cmd.save(stemName+s+".ccp4"); ')
