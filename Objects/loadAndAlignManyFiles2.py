# Description:  To align all of the loaded RNA structures in all possible combinations by their C1' carbon atoms.
# Source:  Generated while helping Miranda Adams at U of Saint Louis.

"""
cmd.do('#  Yes, this construct is a list comprehension inside a list comprehension!;')
cmd.do('run ${1:~/Scripts/}optAlignRNA.py;')
cmd.do('[[optAlignRNA(x, y) for x in cmd.get_names()] for y in cmd.get_names()];')
"""

cmd.do('#  Yes, this construct is a list comprehension inside a list comprehension!;')
cmd.do('run ~/Scripts/optAlignRNA.py;')
cmd.do('[[optAlignRNA(x, y) for x in cmd.get_names()] for y in cmd.get_names()];')
