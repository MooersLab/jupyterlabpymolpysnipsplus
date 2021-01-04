"""
cmd.do('stored.coords = []; ')
cmd.do('iterate_state 1, (resi ${1:101}), stored.coords.append([x,y,z]); ')
cmd.do('[print(i) for i in stored.coords];')
"""
cmd.do('stored.coords = []; ')
cmd.do('iterate_state 1, (resi 101), stored.coords.append([x,y,z]); ')
cmd.do('[print(i) for i in stored.coords];')

# Description:  Print the coordinates of the atoms in a residue.
# Source:  https://www.pymolwiki.org/index.php/Sync

