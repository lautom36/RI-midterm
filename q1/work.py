
# global constants
rLength = .75  # 75 cm
rWidth = .55  # 55 cm

avgVel = 8


def radius(vr, w=rWidth):
    # R(vr) = (w*4)/(vr-8)
    return (w*4)/(vr-8)


def theta_from_vr(vr, w=rWidth):
    # theta. = (vr - vl) / w
    return (vr - vl_from_vr(vr)) / w


def vl_from_vr(vr, v=avgVel):
    # (vl + vr)/2 = v
    # vl = 2v - vr
    return (2*v) - vr


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
        print("Velocites: " + str(vl_from_vr(vr)) + ", " + str(vr) + "\n Radius of turn: " + str(radius(vr)) + "\n Theta: " + str(theta_from_vr(vr)))


# def partB():

# def partC():

partA()
# partB()
# partC()