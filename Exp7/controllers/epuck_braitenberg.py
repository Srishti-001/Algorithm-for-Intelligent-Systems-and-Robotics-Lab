"""
e-puck Braitenberg reactive obstacle avoidance controller.
"""
from controller import Robot

TIME_STEP = 64
MAX_SPEED = 6.28

robot = Robot()
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Infrared sensors
ps = []
for i in range(8):
    sensor = robot.getDevice(f'ps{i}')
    sensor.enable(TIME_STEP)
    ps.append(sensor)

while robot.step(TIME_STEP) != -1:
    ps_vals = [s.getValue() for s in ps]
    # Simple reactive Braitenberg weights
    left_obstacle = ps_vals[5] > 80.0 or ps_vals[6] > 80.0 or ps_vals[7] > 80.0
    right_obstacle = ps_vals[0] > 80.0 or ps_vals[1] > 80.0 or ps_vals[2] > 80.0
    
    if left_obstacle:
        left_speed = 0.5 * MAX_SPEED
        right_speed = -0.5 * MAX_SPEED
    elif right_obstacle:
        left_speed = -0.5 * MAX_SPEED
        right_speed = 0.5 * MAX_SPEED
    else:
        left_speed = 0.7 * MAX_SPEED
        right_speed = 0.7 * MAX_SPEED
        
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
