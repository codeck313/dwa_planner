import math

DT = 0.1
MAX_ACC = 0.3
MAX_VEL =  1.0
MIN_VEL = 0
MAX_YAWRATE = 1.0#40.0 * math.pi / 180.0
MAX_ALPHA = 0.85 #40.0 * math.pi / 180.0
RESO = 0.01
TIME_CALC = 3.0
MAX_DIG_SIZE = 0.8 #1.0 #1.147693339
HEADINGGAIN = 0.5#0.5
OBSTACLEGAIN = 0.8
VELOCITYGAIN = 0.7
DISTANCEGAIN = 0.5#0.1
STUCK = 0.001
GOAL = [4,0]
THRESHOLD = 0.5
LENGTH_ROBOT = 1.2
WIDTH_ROBOT = 0.8
FACTOR = 1.1