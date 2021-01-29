# Description:  Set additional path for PyMOL to search on startup.
# Source:  placeHolder

"""
cmd.do('os.environ["PATH"] += os.pathsep +${1: "/Applications/ATSAS/bin"};')
"""

cmd.do('os.environ["PATH"] += os.pathsep + "/Applications/ATSAS/bin";')
