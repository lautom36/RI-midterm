from cmath import cos, sin, sqrt, pi


def dist(x1, y1, x2=0, y2=0):
    return sqrt(abs(x1-x2)**2 + abs(y1-y2)**2).real

def f_kinematics(vLeft, vRight, x0, y0, theta0, w, dt=0.1):
    xNow = x0 - 1.0/2.0 * (vRight + vLeft) * sin(theta0).real * dt
    yNow = y0 + 1.0/2.0 * (vRight + vLeft) * cos(theta0).real * dt
    thetaNow = theta0 + 1/w * (vRight - vLeft) * dt
    return(xNow, yNow, thetaNow)


def doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, time=[0], theta=[0], width=.3, dt=.1):
    for i in range(int(duration * 10)):
        xNow, yNow, thetaNow = f_kinematics(lwv, rwv, currXPos, currYPos, currTheta, width, dt)
        theta.append((thetaNow - currTheta) / dt)
        currXPos = xNow
        currYPos = yNow
        currTheta = thetaNow
        x.append(xNow)
        y.append(yNow)
        time.append(time[-1] + dt)

    return currXPos, currYPos, currTheta, x, y, theta, time