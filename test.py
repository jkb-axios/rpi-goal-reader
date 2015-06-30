#!/usr/bin/env python

from goal_reader import SERVER_IP, SERVER_PORT, mode_TEST, GoalReader

gr = GoalReader(SERVER_IP,SERVER_PORT,mode_TEST)

# sensor per goal tests
gr.spg_sensor1() # visitor goal

gr.spg_sensor2() # home goal

gr.spg_sensor1() # visitor goal

gr.spg_sensor2() # home goal

# toggle sensor mode
gr.ts_sensor1() # goal scored (visitor)

gr.ts_sensor2() # trigger home goal
gr.ts_sensor1() # goal scored (home)

gr.ts_sensor1() # goal scored (visitor)

gr.ts_sensor2() # trigger home goal
gr.ts_sensor1() # goal scored (home)

# only need this if not using mode_TEST
#gr.cleanup()
