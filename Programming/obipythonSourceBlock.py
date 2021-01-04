"""
cmd.do('#+BEGIN_SRC ipython :session py :kernel pymol.python :exports both :results raw drawer ')
cmd.do('from pymol import cmd')
cmd.do('cmd.do("reinitialize")')
cmd.do('cmd.bg_color("white")')
cmd.do('cmd.do("fetch 6VXX")')
cmd.do('cmd.do("zoom (resi 614 and chain A)")')
cmd.do('cmd.label(selection="chain A and resi 614 and name CB", expression="'%s-%s' % (resn,resi)")')
cmd.do('cmd.do("set label_color, black; set label_size, 48")')
cmd.do('cmd.do("set stick_radius, 0.12")')
cmd.do('cmd.do("hide cartoon; show sticks")')
cmd.do('cmd.do("set ray_shadows, 0")')
cmd.do('cmd.do("draw")')
cmd.do('cmd.do("png /Users/blaine/D614Gipython3.png, 600, 360, dpi=600")')
cmd.do('from IPython.display import Image')
cmd.do('from IPython.core.display import HTML')
cmd.do('PATH = "/Users/blaine/"')
cmd.do('Image(filename = PATH + "D614Gipython3.png", width=600, unconfined=True)')
cmd.do('#+END_SRC')
cmd.do('')
cmd.do('#+RESULTS:')
"""
cmd.do('#+BEGIN_SRC ipython :session py :kernel pymol.python :exports both :results raw drawer ')
cmd.do('from pymol import cmd')
cmd.do('cmd.do("reinitialize")')
cmd.do('cmd.bg_color("white")')
cmd.do('cmd.do("fetch 6VXX")')
cmd.do('cmd.do("zoom (resi 614 and chain A)")')
cmd.do('cmd.label(selection="chain A and resi 614 and name CB", expression="'%s-%s' % (resn,resi)")')
cmd.do('cmd.do("set label_color, black; set label_size, 48")')
cmd.do('cmd.do("set stick_radius, 0.12")')
cmd.do('cmd.do("hide cartoon; show sticks")')
cmd.do('cmd.do("set ray_shadows, 0")')
cmd.do('cmd.do("draw")')
cmd.do('cmd.do("png /Users/blaine/D614Gipython3.png, 600, 360, dpi=600")')
cmd.do('from IPython.display import Image')
cmd.do('from IPython.core.display import HTML')
cmd.do('PATH = "/Users/blaine/"')
cmd.do('Image(filename = PATH + "D614Gipython3.png", width=600, unconfined=True)')
cmd.do('#+END_SRC')
cmd.do('')
cmd.do('#+RESULTS:')

# Description:  Source block template in org-mode with ob-ipython package. 
# Source:  

