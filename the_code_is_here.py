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
