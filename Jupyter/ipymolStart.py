# Description:  Code to start the RPC server with ipymol. Start pymol in terminal with pymol -R; select pymol.python as the kernel in juptyer. You may have to create this kernel for the Python interpreter that is inside PyMOL.
# Source:  placeHolder

"""
cmd.do('from ipymol import viewer as ipv;')
cmd.do('ipv.start() # Start PyMOL RPC server;')
"""

cmd.do('from ipymol import viewer as ipv;')
cmd.do('ipv.start() # Start PyMOL RPC server;')
