# This is from Siraj Ravals video on introduction to OpenAI

import gym
import universe
import random 

def main():

  #init environment
  env = gym.make('flashgames.CoasterRacer-v0')
  #client is the agent
  #remote is the environment (local)
  observation_n = env.reset()

  #init variables
  #num of game iterations
  n = 0
  j = 0

  #sum of observations

  total_sum = 0
  prev_total_sum = 0
  turn = False

  #define our turne/keyboard actions

  left = [('KeyEvent', 'ArrowUp',True),('KeyEvent', 'ArrowLeft',True),('KeyEvent', 'ArrowRight',False)]
  right = [('KeyEvent', 'ArrowUp',True),('KeyEvent', 'ArrowLeft',True),('KeyEvent', 'ArrowRight',False)]
  forward = [('KeyEvent', 'ArrowUp',True),('KeyEvent', 'ArrowLeft',True),('KeyEvent', 'ArrowRight',False)]
  