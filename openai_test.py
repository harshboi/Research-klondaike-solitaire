# This is from Siraj Ravals video on introduction to OpenAI

import gym
import universe
import random 

def determine_turn(turn,observation_n,j,total_sum,prev_total_sum,reward_n):
  #for every 15 iterations, sum the total observations, and take the average
  #if lower than 0, change the direction
  #if we go 15 iterations and get a reward each step, we're doing something right
  #thats when we turn

  if(j>= 15):
    
    if(total_sum/j ) == 0:
      turn = True;
    else:
      turn = False;

    #reset variables
    total_sum = 0
    j = 0
    prev_total_sum = total_sum
    total_sum = 0;


  else:
    turn = False;

  if(observation_n != None):
    #increment counter and reward sum
    j+=1
    total_sum += reward_n
  return(total_sum, j, total_sum, prev_total_sum)



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
  #for formatting purposes in a nut shell
  left = [('KeyEvent', 'ArrowUp',True),('KeyEvent', 'ArrowLeft',True),('KeyEvent', 'ArrowRight',False)]
  right = [('KeyEvent', 'ArrowUp',True),('KeyEvent', 'ArrowLeft',True),('KeyEvent', 'ArrowRight',False)]
  forward = [('KeyEvent', 'ArrowUp',True),('KeyEvent', 'ArrowLeft',True),('KeyEvent', 'ArrowRight',False)]
  
  while True:
    #increment a counter for a number of iterations
    n+=1
    
    if(n>1):
    #if atleast one iteration, check if a turn is needed
      prev_score = reward_n[0]

      #should we turn?
      if(turn):
        #pick a random event
        #where to turn?
        event=random.choice([left,right])
        #perform an action
        action_n = [event for ob in observation_n]
        #set turn to false
        turn = False

    elif(~turn):
      #if no turn is needed, go straight
      action_n = [forward for ob in observation_n]

    #if there is an observation, then game has started, check if turn needed
    if(observation_n[0] != None):
      turn,j,total_sum,prev_total_sum = determine_turn(turn,observation_n[0],j,total_sum,prev_total_sum,reward_n[0])

    #save new variables for each iteration
    observation_n, reward_n, done_n, info = env.step(action_n)

    env.render()


if __name__ == '__main__':
  main()