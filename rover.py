from rrb3 import *
rr = RRB3(9, 6)
rr.set_led1(1)
rr.set_led1(0)
rr.set_led2(1)
rr.set_led2(0)
rr.sw1_closed()

rr.step_forward(.6, 100)  # step in one direction for 200 steps with a 5ms delay between each phase change
rr.set_reverse(.6, 200)   # other direction
rr.forward()       # forward half speed indefinately
rr.forward(5, 1)   # forward for 5 seconds at full speed
rr.left()          #left 
rr.right()         #right
rr.forward()
rr.stop(2)         #stop
