from math import cos, radians, sin


# global constants
m = .2 # kg mass of weight
l = 1.0
M = 4.0 # kg mass of cart

def partA ():
  print('starting partA')
  """
  The acceleration of theta is bassed on the mass ratio

  Acceleration of x is based on force plus theta velocity - the angular forces of the weight
  """

def getForce(xAccel, thetaAccel, theta, thetaVel):
  return (M + m) * xAccel - m * l * thetaAccel * cos(theta) + m * l * thetaVel ** 2 * sin(theta)

def getThetaAccel(force, gravity, theta, thetaVel):
  temp = -force - m * l + thetaVel ** 2 * sin(theta)
  return(gravity * sin(theta) + cos(theta) * temp) / (l * (4.0/3.0 - (m * cos(theta) ** 2) / (m + M)))

def getXAccel(force, theta, thetaVel, thetaAccel):
  return (force + m * l * (thetaVel ** 2 * sin(theta) - thetaAccel * cos(theta))) / (m + M)

def kinInt(x, dt, xVel, xAccel, theta, thetaVel, thetaAccel):
  x = x + dt * xVel
  xVel = xVel + dt * xAccel
  theta = theta + dt * thetaVel
  thetaVel = thetaVel + dt * thetaAccel

  return x, xVel, theta, thetaVel

def partB():
  print('starting partB')
  time = 0
  done = False
  gravity = 9.8 # m/s in theory this is the velocity of the pole
  dt = .01
  criticalAngle = 0
  force = 6

  # starting state
  x = .5
  xVel = .5
  theta = .5
  thetaVel = .5

  while (not done):
    time += dt    
    action = 0
    if (theta > 0 and theta < radians(90)):
      # exert force in the -x direction
      # vel = -6 * theta # as theta gets bigger the velocity increases
      action = -1 * (theta / 90)

    elif (theta > radians(270) and theta < radians(360)):
      # exert force in the +x direction 
      # vel = 6 * (radians(360) - theta) # as the theta gets closer to 360 the velocity decreases
      action = 1 * ((360 - theta) / 90)

    else:
      # could replace with steps to get weight above critical point
      done = True
    
    thetaAccel = getThetaAccel(force * action, gravity, theta, thetaVel)
    xAccel = getXAccel(force * action, theta, thetaVel, thetaAccel)
    x, xVel, theta, thetaVel = kinInt(x, dt, xVel, xAccel, theta, thetaVel, thetaAccel)


    # next x pos

def partC():
  print('starting partC')
  print('The maximum angle is about 32 degrees')
  thetaVel = 0

  # check each angle from 1 to 90, when x > 1 it is beyond recovery
  for i in range(1, 91):
    x = getThetaAccel(6, 9.8, radians(i), thetaVel)
    print('angle: ' + str(i) + ' Accel: ' + str(x))

partC()