#!/bin/env python

from goal_reader import SERVER_IP, SERVER_PORT, mode_TEST, GoalReader

gr = GoalReader(SERVER_IP,SERVER_PORT,mode_TEST)

gr.spg_sensor1()
gr.spg_sensor2()
gr.ts_sensor1()
gr.ts_sensor2()
