
# global constants
rLength = .75  # 75 cm
rWidth = .55  # 55 cm

avgVel = 8


def radius(vr):
    # R(vr) = 2.2/(vr-8)
    return 2.2/(vr-8)


def vl_from_vr(vr):
    return 16 - vr


def partA():
    # circle diameter of 5m
    # start at (0,0)
    # constant velocity of 8m/s
    dt = .1
    diameter = 5
    turn_time = 3
    steps = int(turn_time / dt)
    for i in range(steps):
        vr = i*((diameter / 2) / turn_time)
        print("Velocites: " + str(vl_from_vr(vr)) + ", " + str(vr) + "\n Radius of turn: " + str(radius(vr)))



# def partB():

# def partC():

partA()
# partB()
# partC()