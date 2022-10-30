import math
import time
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

def f_kinematics(vLeft, vRight, x0, y0, theta0, w, dt=0.1):
    xNow = x0 - 1.0/2.0 * (vRight + vLeft) * math.sin(theta0) * dt
    yNow = y0 + 1.0/2.0 * (vRight + vLeft) * math.cos(theta0) * dt
    thetaNow = theta0 + 1/w * (vRight - vLeft) * dt
    return(xNow, yNow, thetaNow)

def partA():
    # circle diameter of 5m
    # start at (0,0)
    # constant velocity of 8m/s
    dt = .1
    width = .55
    diameter = 5
    times, xs, ys, thetas = [0], [0], [0], [0]
    currX, currY, currTheta = 0, 0, 0

    # get to edge of cicle
    rwv = 9.76
    lwv = 6.24
    for i in range(5):
        xNow, yNow, thetaNow = f_kinematics(lwv, rwv, currX, currY, currTheta, width, dt)
        thetas.append((thetaNow - currTheta) / dt)
        currX, currY, currTheta = xNow, yNow, thetaNow
        xs.append(xNow)
        ys.append(yNow)
        times.append(times[-1] + dt)

    # follow circle
    rwv = 8.88
    lwv = 7.12
    for i in range(20):
        xNow, yNow, thetaNow = f_kinematics(lwv, rwv, currX, currY, currTheta, width, dt)
        thetas.append((thetaNow - currTheta) / dt)
        currX, currY, currTheta = xNow, yNow, thetaNow
        xs.append(xNow)
        ys.append(yNow)
        times.append(times[-1] + dt)

    times.pop()
    thetas.pop()
    plot(xs, ys, "x position", "y position", "Position")
    dx = [(xs[i+1]-xs[i])/dt for i in range(len(xs) - 1)]
    plot(times, dx, "time", "trajectory, X trajectory")
    dy = [(ys[i+1]-ys[i])/dt for i in range(len(ys) - 1)]
    plot(times, dy, "time", "trajectory, Y trajectory")
    plot(times, thetas, "time",  "angular velocity", "Angular Velocity as a Fuction of Time")

    # Stay on circle edge
    circumference = math.pi*diameter

# start part B
def acerman(x0, y0, theta0, alpha, vrw, L, dt=.1):
    x1 = x0 + (-vrw) * math.sin(theta0) * dt
    y1 = y0 + (vrw) * math.cos(theta0) * dt
    theta1 = theta0 + (vrw/L) * math.tan(alpha) * dt
    return x1, y1, theta1

def degToRad(theta):
    return (theta * (math.pi/180))

def partB(dtMulti = 1):
    dt = .1 / dtMulti
    xs, ys, thetas, time = [0], [0], [0], [0]
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
        time.append(time[-1] + dt)
        thetas.append(theta)

    # go around cirlce
    alpha = math.radians(16.7)
    for i in range(20 * dtMulti):
        x, y, theta = acerman(currX, currY, currTheta, alpha, vrw, L, dt)
        currX, currY, currTheta = x, y, theta
        xs.append(x)
        ys.append(y)
        time.append(time[-1] + dt)
        thetas.append(theta)

    time.pop()
    thetas.pop()
    plot(xs, ys, "x position", "y position", "Position")
    dx = [(xs[i+1]-xs[i])/dt for i in range(len(xs) - 1)]
    plot(time, dx, "time", "trajectory, X trajectory")
    dy = [(ys[i+1]-ys[i])/dt for i in range(len(ys) - 1)]
    plot(time, dy, "time", "trajectory, Y trajectory")
    plot(time, thetas, "time",  "angular velocity", "Angular Velocity as a Fuction of Time")
# end part B

# start part c
def findXYFromLocationAngle(theta ,totalDist):
    y = math.sin(theta) * totalDist
    x = math.cos(theta) * totalDist
    return x, y

def findLocationAngle(circum, totalDist):
    return (totalDist / circum) * 360

def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

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
    for i in range(len(xRobot)):
        error = distance(xRobot[i], xActual[i], yRobot[i], yActual[i])
        errors.append(error)
        times.append(i)
    return errors, times

def partC():
    start = time.time()
    dt = 1
    xRobot, yRobot = forwardEuler(dt, math.radians(16.7), 8, rLength)
    xActual, yActual = findActual(dt, 8)
    print(str(len(xRobot)) + " " + str(len(xActual)))
    errors1, times1 = findError(xRobot, yRobot, xActual, yActual, dt)
    end = time.time()
    took1 = (end - start) * 10**3
    print("took: " + str(took1) + "ms")

    start = time.time()
    dt = .1
    xRobot, yRobot = forwardEuler(dt, math.radians(16.7), 8, rLength)
    xActual, yActual = findActual(dt, 8)
    print(str(len(xRobot)) + " " + str(len(xActual)))
    errors2, times2 = findError(xRobot, yRobot, xActual, yActual, dt)
    end = time.time()
    took2 = (end - start) * 10**3
    print("took: " + str(took2) + "ms")

    start = time.time() 
    dt = .01
    xRobot, yRobot = forwardEuler(dt, math.radians(16.7), 8, rLength)
    xActual, yActual = findActual(dt, 8)
    print(str(len(xRobot)) + " " + str(len(xActual)))
    errors3, times3 = findError(xRobot, yRobot, xActual, yActual, dt)
    end = time.time()
    took3 = (end - start) * 10**3
    print("took: " + str(took3) + "ms")

# first plot
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

# second plot
    data = {'dt  =1':took1, 'dt = .1':took2, 'dt = .01':took3}
    tags = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure()
    
    # creating the bar plot
    plt.bar(tags, values, width = 0.4)
    
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")
    plt.show()
    print()

# end part c

# partA()
# partB()
partC()