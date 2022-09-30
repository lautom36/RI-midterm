
import cmath
import utilities.plot

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


def x_pos(vr, x0=0, theta0=0, dt=.1):
    # x_(t+1) = x0 - (1/2)(vr + vl)sin(theta0)dt
    return x0 - (1/2)*(vr + vl_from_vr(vr))*cmath.sin(theta0)*dt


def y_pos(vr, y0=0, theta0=0, dt=.1):
    # y_(t+1) = y0 - (1/2)(vr + vl)cos(theta0)dt
    return y0 - (1/2)*(vr + vl_from_vr(vr))*cmath.sin(theta0)*dt


def partA():
    # circle diameter of 5m
    # start at (0,0)
    # constant velocity of 8m/s
    dt = .1
    diameter = 5
    times = []
    xs = [0]
    ys = [0]

    # Traverse to edge of circle
    turn_time = 3  # seconds
    steps = int(turn_time / dt)
    for i in range(steps):
        vr = i*((diameter / 2) / turn_time)
        vl = vl_from_vr(vr)
        r = radius(vr)
        theta = theta_from_vr(vr)
        xt = x_pos(vr)
        yt = y_pos(vr)
        times.append(i*((diameter / 2) / turn_time))
        xs.append(xt)
        ys.append(yt)
        print("Velocites: " + str(vl) + ", " + str(vr) + "\n Radius of turn: " + str(r) + "\n Theta: " + str(theta))
    # plot(xs, ys)

    # Stay on circle edge
    circumference = cmath.pi*diameter



# def partB():

# def partC():

partA()
# partB()
# partC()