# Description:  Average the B-factors by using a regular list as opposed to a stored list in PyMOL. Edit the selection as needed. 
# Source:  placeHolder

"""
cmd.do('Bfactors = []; ')
cmd.do('#  >>> edit the selection below, which is a range of residue numbers here.;')
cmd.do('iterate (resi ${1:133}), Bfactors.append(b);')
cmd.do('print("Sum = ", "%.2f" % (sum(Bfactors)));')
cmd.do('print("Number of atoms = ", len(Bfactors));')
cmd.do('print( "Average B =" , "%.2f" % ( sum(Bfactors)/float(len(Bfactors))));')
"""

cmd.do('Bfactors = []; ')
cmd.do('#  >>> edit the selection below, which is a range of residue numbers here.;')
cmd.do('iterate (resi 133), Bfactors.append(b);')
cmd.do('print("Sum = ", "%.2f" % (sum(Bfactors)));')
cmd.do('print("Number of atoms = ", len(Bfactors));')
cmd.do('print( "Average B =" , "%.2f" % ( sum(Bfactors)/float(len(Bfactors))));')
