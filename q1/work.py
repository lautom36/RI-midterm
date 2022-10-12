
import math
from utilities.plot import plot

# global constants
rLength = .75  # 75 cm
rWidth = .55  # 55 cm

avgVel = 8


def radius(vr, w=rWidth):
    # R(vr) = (w*4)/(vr-8)
    return (w*4)/(vr-8)


def theta_from_vr(vr, theta0=0, dt=.1, w=rWidth):
    # theta. = (vr - vl) / w
    return theta0 + (1/w)*(vr - vl_from_vr(vr))*dt


def vl_from_vr(vr, v=avgVel):
    # (vl + vr)/2 = v
    # vl = 2v - vr
    return (2*v) - vr


def x_pos(vr, x0=0, theta0=0, dt=.1):
    # x_(t+1) = x0 - (1/2)(vr + vl)sin(theta0)dt
    return x0 - (1/2)*(vr + vl_from_vr(vr))*math.sin(theta0)*dt


def y_pos(vr, y0=0, theta0=0, dt=.1):
    # y_(t+1) = y0 - (1/2)(vr + vl)cos(theta0)dt
    return y0 + (1/2)*(vr + vl_from_vr(vr))*math.cos(theta0)*dt


def partA():
    # circle diameter of 5m
    # start at (0,0)
    # constant velocity of 8m/s
    dt = .1
    diameter = 5
    times = [0]
    xs = [0]
    ys = [0]
    thetas = [0]

    # Traverse to edge of circle
    turn_time = 3  # seconds
    steps = int(turn_time / dt)
def partA():
    # circle diameter of 5m
    # start at (0,0)
    # constant velocity of 8m/s
    dt = .1
    diameter = 5
    times = [0]
    xs = [0]
    ys = [0]
    thetas = [0]

    # Traverse to edge of circle
    turn_time = 3  # seconds
    steps = int(turn_time / dt)
    for i in range(5):
        dist_to_dia = math.sqrt(xs[-1]**2 + ys[-1]**2)
        vr = ((diameter / 2) - dist_to_dia) / turn_time
        vl = vl_from_vr(vr)
        r = radius(vr)
        theta = theta_from_vr(vr, theta0=thetas[-1])
        xt = x_pos(vr, x0=xs[-1], theta0=thetas[-1])
        yt = y_pos(vr, y0=ys[-1], theta0=thetas[-1])
        times.append(i*((diameter / 2) / turn_time))
        xs.append(xt)
        ys.append(yt)
        thetas.append(theta)
        print("Velocites: " + str(vl) + ", " + str(vr) + "\n Radius of turn: " + str(r) + "\n Theta: " + str(theta))
    plot(xs, ys)

    # Stay on circle edge
    circumference = math.pi*diameter


def acerman(x0, y0, theta0, alpha, vrw, L, dt=.1):
    x1 = x0 + (-vrw) * math.sin(theta0) * dt
    y1 = y0 + (vrw) * math.cos(theta0) * dt
    theta1 = theta0 + (vrw/L) * math.tan(alpha) * dt
    return x1, y1, theta1

def degToRad(theta):
    return (theta * (math.pi/180))

def partB():
    xs, ys, thetas = [0], [0], [0]
    alpha = math.radians(10)
    L = rLength
    vrw = avgVel

    currX = 0
    currY = 0
    currTheta = 0

    for i in range(15):
        x, y, theta = acerman(currX, currY, currTheta, alpha, vrw, L,)
        currX, currY, currTheta = x, y, theta
        xs.append(x)
        ys.append(y)
        thetas.append(theta)
        print("x: " + str(x) + " y: " + str(y) + " theta: " + str(theta))

    print(.3246 + (-8) * math.sin(5.225) * .1)
    plot(xs, ys)
# def partC():

partA()
# partB()
# partC()