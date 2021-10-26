# Tello-Drone-Project-Baisc-Movement
This program should make the Tello Drone take off, move up, move forward, go back to its original position, and then fly in a square pattern. Enjoy!

from djitellopy import Tello

tello = Tello()

tello.connect()
tello.take_off()

tello.move_up(90)
tello.move_forward(100)

tello.rotate_counter_clockwise(180)
tello.move_forward(100)

tello.rotate_counter_clockwise(90)
tello.move_forward(30)
tello.rotate_counter_clockwise(90)
tello.move_forward(30)
tello.rotate_counter_clockwise(90)
tello.move_forward(30)
tello.rotate_counter_clockwise(90)
tello.move_forward(30)

tello.land()
