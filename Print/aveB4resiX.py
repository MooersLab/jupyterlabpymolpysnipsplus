# Description:  Prints the residue number and the average bfactor. Uses reduce and lambda, builtin Python functional porgramming functions. Note that you need to convert the length of the list of Bfactors from an integer to a float before division into the sum.
# Source:  placeHolder

"""
cmd.do('')
cmd.do('# ; ')
cmd.do('Bfactors = [];')
cmd.do('# edit the selection below, which is a range of residue numbers here.;')
cmd.do('iterate (resi ${1:133}), Bfactors.append(b);')
cmd.do('print( "Average B-factor of residue ", %{1:133} , "   = ", "%.2f" %(reduce(lambda x, y: x + y, Bfactors) / float(len(Bfactors))) );')
"""

cmd.do('')
cmd.do('# ; ')
cmd.do('Bfactors = [];')
cmd.do('# edit the selection below, which is a range of residue numbers here.;')
cmd.do('iterate (resi 133), Bfactors.append(b);')
cmd.do('print( "Average B-factor of residue ", %{1:133 , "   = ", "%.2f" %(reduce(lambda x, y: x + y, Bfactors) / float(len(Bfactors))) );')
