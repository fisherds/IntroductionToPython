"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Dave Fisher.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

import rosegraphics as rg

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

window = rg.TurtleWindow()

dave = rg.SimpleTurtle('turtle')
dave.speed = 20
dave.pen = rg.Pen('red4', 5)
for k in range(8):
    dave.left(45)
    dave.forward(50)

dave.pen_up()

bob = rg.SimpleTurtle('turtle')
bob.speed = 20
bob.pen = rg.Pen('green', 5)
bob.pen_up()
bob.backward(75)
bob.left(90)
bob.forward(75)
bob.right(90)
bob.pen_down()
for k in range(3):
    bob.forward(100)
    bob.right(120)

window.close_on_mouse_click()
