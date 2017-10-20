from US import US
import Movement

def main():
    sensorB = US(20, 21)
    sensorT = US(5, 6)

    while (sensorB.getDistance() < 15 or sensorT.getDistance() < 15):
        Movement.move_forward()
    Movement.stop_movement()



