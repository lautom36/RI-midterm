from locale import currency


def partC():
  # imports
  from sklearn.preprocessing import KBinsDiscretizer
  import numpy as np 
  import math
  from typing import Tuple
  import gym

  # setup cart environmet
  env = gym.make("CartPole-v1")

  bins = (6, 12)
  lowerBounds = [env.observation_space.low[2], -math.radians(50)]
  upperBounds = [env.observation_space.high[2], math.radians(50)]

  # turn coninues states into discrete ones
  def toDiscrete(theta, thetaVel):
    est = KBinsDiscretizer(n_bins=bins, encode='ordinal', strategy='uniform')
    est.fit([lowerBounds, upperBounds])
    return tuple(map(int, est.transform([[theta, thetaVel]])[0]))

  # create the q table
  QTable = np.zeros(bins + (env.action_space.n,))

  # get the greedy q value
  def getGreedy(state):
    return np.argmax(QTable[state])

  # update the Q table
  def updateQTable(reward, newState, discount=1):
    bestVal = np.max(QTable[newState])
    learnedVal = reward + discount * bestVal
    return learnedVal

  # get current learning and exploration rates
  def getRates(itt, minLearnRate=.01, minExplorRate=.1):
    learningRate = max(minLearnRate, min(1.0, 1.0 - math.log10((itt + 1) / 25)))
    exploreRate = max(minExplorRate, min(1.0, 1.0 - math.log10((itt + 1) / 25)))
    return learningRate, exploreRate

  Itterations = 10000
  for itt in range(Itterations):
    observations = env.reset()[0][slice(2,4)]
    currState = toDiscrete(theta=observations[0], thetaVel=observations[1])
    done = False
  
    while not done:
      # get rates
      learningRate, exploreRate = getRates(itt)

      # see if instead of being greedy we explore
      action = None
      if np.random.random() < exploreRate:
        action = env.action_space.sample()
      # take the greedy action
      else:
        action = getGreedy(currState)

      # do the action
      observations, reward, done, _, _ = env.step(action)
      observations = observations[slice(2,4)]
      newState = toDiscrete(theta=observations[0], thetaVel=observations[1])

      # use the new state to update the Q Table
      learnedValue = updateQTable(reward, newState)
      prevValue = QTable[currState][action]
      QTable[currState][action] = (1 - learningRate) * prevValue + learningRate * learnedValue 

      # update state
      currState = newState

      # show the env
      env.render()
  env.close()



partC()