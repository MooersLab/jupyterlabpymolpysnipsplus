# Description:  Hide the partially occupied atoms with the part b alternate locator.
# Source:  placeHolder

"""
cmd.do('select altconf, alt ${1:b}  # select B alternative locators;')
cmd.do('hide everything, altconf  # hide alt B locators;')
"""

cmd.do('select altconf, alt b  # select B alternative locators;')
cmd.do('hide everything, altconf  # hide alt B locators;')
