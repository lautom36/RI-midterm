
from cProfile import label
import math
import matplotlib.pyplot as plt


def plot(x, y, xName = 'x - axis', yName = 'y - axis', plotName = 'plot'):
    # plot points
    plt.plot(x,y)

    # rename axises
    plt.xlabel(xName)
    plt.ylabel(yName)

    # set graph title
    plt.title(plotName)

    # show graph
    plt.show()

def plotWithCircle(x, y, radius, xName = 'x - axis', yName = 'y - axis', plotName = 'plot'):
    fig=plt.figure()
    ax=fig.add_subplot()
        # plot points
    plt.plot(x,y, label = "Robot Path")

    circle = plt.Circle((0,0), radius, fill= False, label = "circle")
    centreSpot = plt.Circle((0,0),0.05,color="black")
    ax.add_patch(circle)
    ax.add_patch(centreSpot)

    # circle2 = plt.Circle((-1.25,0), radius/2, fill= False, label = "circle")
    # centreSpot2 = plt.Circle((-1.25,0),0.05,color="black")
    # ax.add_patch(circle2)
    # ax.add_patch(centreSpot2)

    # rename axises
    plt.xlabel(xName)
    plt.ylabel(yName)

    # set graph title
    plt.title(plotName)
    plt.legend()

    # show graph
    plt.show()

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

def partB(dtMulti = 1):
    dt = .1 / dtMulti
    xs, ys, thetas = [0], [0], [0]
    L = rLength
    vrw = avgVel

    currX = 0
    currY = 0
    currTheta = 0

    alpha = math.radians(30.96)
    # get to edge of circle
    for i in range(5 * dtMulti):
        x, y, theta = acerman(currX, currY, currTheta, alpha, vrw, L, dt)
        currX, currY, currTheta = x, y, theta
        xs.append(x)
        ys.append(y)
        thetas.append(theta)
        print("x: " + str(x) + " y: " + str(y) + " theta: " + str(math.degrees(theta)))

    # go around cirlce
    alpha = math.radians(16.7)
    for i in range(20 * dtMulti):
        x, y, theta = acerman(currX, currY, currTheta, alpha, vrw, L, dt)
        currX, currY, currTheta = x, y, theta
        xs.append(x)
        ys.append(y)
        thetas.append(theta)

    # print(.3246 + (-8) * math.sin(5.225) * .1)
    # plotWithCircle(xs, ys, 2.5)
    plot(xs, ys)

dtMulti = 1

def findXYFromLocationAngle(theta ,totalDist):
    y = math.sin(theta) * totalDist
    x = math.cos(theta) * totalDist
    return x, y

def findLocationAngle(circum, totalDist):
    return (totalDist / circum) * 360

def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# def partCHelper(dt):
#     circumference = 5 * math.pi
#     totalDist = 0
#     xAct, yAct = [2.5], [0]
#     totalError = 0
#     errors = []
#     times= []
#     currTime = 0.0

#     # start at edge of circle
#     xs, ys, thetas = [2.5], [0], [0]
#     L = rLength
#     vrw = avgVel

#     currX = 2.5
#     currY = 0
#     currTheta = 0

#     # go around cirlce
#     alpha = math.radians(16.7)
#     for i in range(int(10 / dt)):
#         x, y, theta = acerman(currX, currY, currTheta, alpha, vrw, L, dt)
#         currX, currY, currTheta = x, y, theta
#         xs.append(x)
#         ys.append(y)
#         thetas.append(theta)

#         # find x, y, and theta actual
#         totalDist += vrw * dt
#         locAngle = findLocationAngle(circumference, totalDist)
#         xActual, yActual = findXYFromLocationAngle(locAngle, totalDist)
#         xAct.append(xActual)
#         yAct.append(yActual)

#         currTime = float(i * dt)

#         if(currTime.is_integer()):
#             totalError += distance(x, xActual, y, yActual)
#             errors.append(totalError)
#             times.append(i*dt)

#     return times, errors

def forwardEuler(dt, alpha, vrw, L, startX = 0, startY = 0, startTheta = 0):
    T = dt
    x, y, theta = startX, startY, startTheta
    xs = [2.5]
    ys = [0]
    thetas = [0]

    xReturn = [0]
    yReturn = [0]
    for k in range(1,10):
        for i in range(int(1 / dt)):
            xNew = xs[-1] - T * vrw * math.sin(thetas[-1])
            yNew = ys[-1] + T * vrw * math.cos(thetas[-1])
            thetaNew = thetas[-1] + T * (vrw / L ) * math.tan(alpha) 
            x, y, theta = xNew, yNew, thetaNew
            xs.append(x)
            ys.append(y)
            thetas.append(theta)
        xReturn.append(x)
        yReturn.append(y)

    # plotWithCircle(xs, ys, 2.5)

    return xReturn, yReturn

def findActual(dt, vrw):
    xAct, yAct = [0], [0]
    circumference = 5 * math.pi
    totalDist = 0

    for k in range(1, 10):
        for i in range(int(1 / dt)):
            totalDist += vrw * dt
            locAngle = findLocationAngle(circumference, totalDist)
            xActual, yActual = findXYFromLocationAngle(locAngle, totalDist)
            xAct.append(xActual)
            yAct.append(yActual)
    return xAct, yAct

def findError(xRobot, yRobot, xActual, yActual, dt):
    errors = []
    times = []
    totalError = 0
    for i in range(len(xRobot)):
        totalError += distance(xRobot[i], xActual[i], yRobot[i], yActual[i])
        errors.append(totalError)
        times.append(i)
    return errors, times

def partC():
    dt = 1
    xRobot, yRobot = forwardEuler(dt, math.radians(16.7), 8, rLength)
    xActual, yActual = findActual(dt, 8)
    print(str(len(xRobot)) + " " + str(len(xActual)))
    errors1, times1 = findError(xRobot, yRobot, xActual, yActual, dt)
    print(len(errors1))

    dt = .1
    xRobot, yRobot = forwardEuler(dt, math.radians(16.7), 8, rLength)
    xActual, yActual = findActual(dt, 8)
    print(str(len(xRobot)) + " " + str(len(xActual)))
    errors2, times2 = findError(xRobot, yRobot, xActual, yActual, dt)
    print(len(errors2))

    dt = .01
    xRobot, yRobot = forwardEuler(dt, math.radians(16.7), 8, rLength)
    xActual, yActual = findActual(dt, 8)
    print(str(len(xRobot)) + " " + str(len(xActual)))
    errors3, times3 = findError(xRobot, yRobot, xActual, yActual, dt)
    print(len(errors3))

    plt.plot(times1,errors1, label="dt = 1")
    plt.plot(times2, errors2, label="dt = .1")
    plt.plot(times3, errors3,label="dt = .01")

    # rename axises
    plt.xlabel("time")
    plt.ylabel("error")

    # set graph title
    plt.title("")
    plt.legend()

    # show graph
    plt.show()





# partA()
# partB(1000)
partC()