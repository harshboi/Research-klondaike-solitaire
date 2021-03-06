import random
import math
import pdb
from itertools import chain
import copy
import time
import sys, os
global str



  # fix the tableau_tableau function to move stacks of more than 9 cards: faceup_card = int(action[3]+int(action4)) will fail for 10 or more cards due to index conversion problems
  # fix the scoring function, awarding extra points for bad moves makes them take precedence (ex: stacks moved in a tableau (for sure awarding more as a simple multiple is being used for awarding points rather than 
  # checking the number of cards made face up))
  
  # fix the multiple number argument error in action. Ex: op_t18 ->tableau6 will be read as op_t1 ->tableau6



    # (Pdb) card = state.current_state.open_talon[open_talon_card]
    # (Pdb) card
    # ['D', 'R', 9, 0, 0, 0]
    # (Pdb) action
    # 'op_t18 ->tableau3'
    # (Pdb) state.current_state.open_talon[18]
    # ['H', 'R', 5, 0, 0, 0]
    # (Pdb) state.current_state.tableau[3]
    # [['D', 'R', 1, 0, 0, 0], ['C', 'B', 9, 0, 0, 0], ['C', 'B', 3, 0, 0, 0], ['D', 'R', 7, 0, 1, 0], ['S', 'B', 6, 0, 1, 0]]
    # (Pdb) open_talon_card
    # 1
    # (Pdb) action
    # 'op_t18 ->tableau3'

  # Fix the open talon to foundation: Make the 4th argument of the array 1 that is the card has been discovered by the simulator
  # fixed class nonetype issue - Make sure self.return_calling() being called over self.calling()

# Traceback (most recent call last):
#   File "runner.py", line 9, in <module>
#     from dealers import *
#   File "../dealers/native_dealer.py", line 73, in run
#     self.run_trials(multiprocess_mode=multiprocess_mode)
#   File "../dealers/native_dealer.py", line 154, in run_trials
#     game_outputs.append(self.run_trial())
#   File "../dealers/native_dealer.py", line 193, in run_trial
#     action_to_take = self.agents[current_state.current_player].select_action(current_state)
#   File "../agents/frameworks/recursive_bandit_framework.py", line 26, in select_action
#     return self.estimateV(state, self.depth)[1]  # return the best action
#   File "../agents/frameworks/recursive_bandit_framework.py", line 55, in estimateV
#     arm_data = self.run_pull(state, bandit, depth)
#   File "../agents/frameworks/recursive_bandit_framework.py", line 75, in run_pull
#     future_reward = self.estimateV(current_state, depth - 1)[0]  # [0] references the q_values for best action
#   File "../agents/frameworks/recursive_bandit_framework.py", line 34, in estimateV
#     return self.evaluation.evaluate(state), None  # no more depth, so default to the evaluation fn
#   File "../agents/evaluations/rollout_evaluation.py", line 19, in evaluate
#     total_rewards += self.run_rollout(state)
#   File "../agents/evaluations/rollout_evaluation.py", line 31, in run_rollout
#     action = self.rollout_policy.select_action(sim_state)
#   File "../agents/random_agent.py", line 19, in select_action
#     raise ValueError("Action count cannot be zero.")
# ValueError: Action count cannot be zero.
# Run with  runner.py from chess.py and check when cached actions is 0
# Error: self.open_talon went to length 0 suddenly on executing action opt_t to f
# Error in is_legal pattern matching or some shit in open_talon related stuff, Fix
# Work on is open function -- Function for moving multiple face up cards
# Add a function for moving multiple cards -- Multiple faceup cards at the same time (specifying the action)
# Reducing complexity by removing memoize and adding an extra dimension for storage in the array
# self.talon has a card that self.foundation does, check distribution of cards -- Done - Resolved
# Errors below have all been fixed

# Error 2: Work on it later
# pygame 1.9.4
# Hello from the pygame community. https://www.pygame.org/contribute.html
# > /home/darkice/AI/PyPlan/dealers/simulators/solitaire.py(18)__init__()
# -> self.current_state = solitaire.game()
# (Pdb) c
# agents part
# > /home/darkice/AI/PyPlan/dealers/native_dealer.py(48)configure()
# -> self.num_trials = num_trials
# (Pdb) c
# --Return--                                                                                                                                                                                                        |
# > /home/darkice/AI/PyPlan/dealers/simulators/solitaire.py(33)reinitialize()->None
# -> pdb.set_trace()
# (Pdb) c
# Traceback (most recent call last):
#   File "runner.py", line 9, in <module>
#     from dealers import *
#   File "../dealers/native_dealer.py", line 73, in run
#     self.run_trials(multiprocess_mode=multiprocess_mode)
#   File "../dealers/native_dealer.py", line 154, in run_trials
#     game_outputs.append(self.run_trial())
#   File "../dealers/native_dealer.py", line 191, in run_trial
#     action_to_take = self.agents[current_state.current_player].select_action(current_state)
#   File "../agents/frameworks/recursive_bandit_framework.py", line 26, in select_action
#     return self.estimateV(state, self.depth)[1]  # return the best action
#   File "../agents/frameworks/recursive_bandit_framework.py", line 55, in estimateV
#     arm_data = self.run_pull(state, bandit, depth)
#   File "../agents/frameworks/recursive_bandit_framework.py", line 71, in run_pull
#     chosen_arm = bandit.select_pull_arm()
#   File "../agents/bandits/uniform_bandit.py", line 10, in select_pull_arm
#     return self.num_pulls.argmin()
# ValueError: attempt to get argmin of an empty sequence

  # len(self.stock) = 45 ?? should be 24
  # commented line 194 in native_dealer.py
  # Line 427 error
    #   File "../dealers/simulators/solitairecode/solitaire.py", line 427, in is_legal
    #     top_tableau_card = self.tableau[tableau_num][-1]
    # IndexError: list index out of range
  # code handle it
  # Integrate with Alex's codes
possible_actions = []
class game:
  def __init__(self):
    #self.cards = {'K':[['B','S'],['B','C'],['R','D'],['R','D']],"Q":[['B','S'],['B','C'],['R','D'],['R','D']],"J":[['B','S'],['B','C'],['R','D'],['R','D']],"A":[['B','S'],['B','C'],['R','D'],['R','D']],"2":[['B','S'],['B','C'],['R','D'],['R','D']],"3":[['B','S'],['B','C'],['R','D'],['R','D']]}
    #self.cards.update({"4":[['B','S'],['B','C'],['R','D'],['R','D']],"5":[['B','S'],['B','C'],['R','D'],['R','D']],"6":[['B','S'],['B','C'],['R','D'],['R','D']],"7":[['B','S'],['B','C'],['R','D'],['R','D']],"8":[['B','S'],['B','C'],['R','D'],['R','D']],"9":[['B','S'],['B','C'],['R','D'],['R','D']],"10":[['B','S'],['B','C'],['R','D'],['R','D']]})
    #self.cards.update({"A":[['B','S'],['B','C'],['R','D'],['R','D']]})
      self.tempp = 0
      self.cards = []     # NOT USED, REMOVE
      self.tcards = []    # NOT USED PRESENTLY, JUST HOLDS A COPY OF EVERYTHING
      self.stock = []                             # Contains the decked to be flipped
      self.foundation = [[],[],[],[]]
      self.talon = []                            # Contains flipped cards
      self.tableau = [[],[],[],[],[],[],[]]       # 7 cards laid out aside eachother
      # self.shuffle()
      self.score = 0
      self.stock_resets = 0
      self.last_action = None
      self.cached_actions = [] # should be updated by an outside simulator
      self.length = len(self.stock) + len(self.talon)+len(self.tableau[0])+len(self.tableau[1])+len(self.tableau[2])+len(self.tableau[3])+len(self.tableau[4])+len(self.tableau[5])+len(self.tableau[6])+len(self.foundation[0])+len(self.foundation[1])+len(self.foundation[2])+len(self.foundation[3])
      # self.memoize = []
      self.actions = []
      self.second_last_action = None    # Is used for checking the second last card moved to prevent loops caused by repeating actions
      self.past_actions = []
      self.open_talon = []
      self.return_game_state = 0

  def shuffle(self):
    n = []
    for i in range(1,11):
      n.append(['D','R',i,0,0,0])  # First 0 for stopping rewarding points for the same card being oscillated again, second 0 for stating whether a card is known or not
      n.append(['H','R',i,0,0,0])  #third 0 for showing that multiple cards are face up together
      n.append(['S','B',i,0,0,0])
      n.append(['C','B',i,0,0,0])

    face_cards = ["K","Q","K","A"]
    for i in range(11,14):
      n.append(['C','B',i,0,0,0])  #third 0 for showing that multiple cards are face up together
      # n.append(['C','B',""+face_cards[i-10]])   1 - A, 11 - J, 12 - Q, 13 - K
      n.append(['S','B',i,0,0,0])
      n.append(['D','R',i,0,0,0])
      n.append(['H','R',i,0,0,0])

    #for i in range(1,26):
    self.cards = n
    self.tcards = n
    self.assign_tableau(n)
    self.create_stock()
    self.playable_stock()

    #insert code

  def get_length(self):
    self.length = len(self.stock) + len(self.talon)+len(self.tableau[0])+len(self.tableau[1])+len(self.tableau[2])+len(self.tableau[3])+len(self.tableau[4])+len(self.tableau[5])+len(self.tableau[6])+len(self.foundation[0])+len(self.foundation[1])+len(self.foundation[2])+len(self.foundation[3])
    print(self.length)


  #########################################################################################################
  # Name: assign_tableau
  # Use: Used for filling up the tableau
  # Paramterers: the list with all card combinations
  #########################################################################################################
  def assign_tableau(self,n):
    tableau_num = 0
    self.tempp += 1
    self.foundation = [[],[],[],[]]
    self.tableau = [[],[],[],[],[],[],[]]       # 7 cards laid out aside eachother
    for i in range(0,28):      # For each tableau
      # time.sleep(1)
      x = random.randint(0,len(n)-1)   # Contains the card number
      # print("x is " + str(x) + " len of x  is " + str(len(n)) + "\n")
      card = n[x]                    # Stores a copy of the card
      if(len(self.tableau[tableau_num]) < tableau_num+1):
        self.tableau[tableau_num].append(card)
        if(len(self.tableau[tableau_num]) == tableau_num+1):
          tableau_num += 1

      n.pop(x)
    for i in range(7):
      self.tableau[i][-1][4] = 1    # Makes the last card a face up card

    self.cards = n


  def create_stock(self):
    self.stock = []
    for i in range(0,24):                           # CHANGE TO WHILE LOOP, perform testing (Mostly works)
      #pdb.set_trace()
      x = random.randint(0,len(self.cards)-1)
      self.stock.append(self.cards[x])
      self.cards.pop(x)

  #########################################################################################################
  # Prints the instructions
  #########################################################################################################

  def instructions(self):
    self.UI()
    if(len(self.stock)>0 or len(self.talon)>0):
      print("1 to Flip the stock")                                            # Function Created

    if(len(self.talon)>0):
      print("2 to move a card from the talon to the tableau")              # Function Created
      print("3 to move a card from the tableau to the foundation")             # Created but not checked
      print("4 to move a card from the talon to the foundation")
      print("5 to move a card from the tableau to the tableau")
    if(len(self.stock)<3):
      print("Press 4 to flip all the cards from talon back to stock")         # Function Created

    choice = input("Choice ")
    choice = int(choice)
    if(choice == 1):
      self.flip_stock()
      #print UI stuff
    elif(choice == 2):
      tableau_num = input("Enter the tableau number (0-6) to move to ")
      tableau_num = int(tableau_num)
      res = self.tableau_addition(tableau_num)
      if(res == 0):
        print("Operation not possible")
      # elif(res == 1):
        #Print UI
        # self.UI()
    elif(choice ==3):
      tableau_num = input("Enter the tableau to move the card from (0-6)")
      tableau_num = int(tableau_num)
      foundation_num = input("Enter the foundation to move the card to (0-3) ")
      foundation_num = int(foundation_num)
      self.tableau_to_foundation(tableau_num,foundation_num)
    elif(choice ==4):
      self.talon_to_stock()
    elif(choice == 5):
      # _loop = 0
      # while(_loop == 0):
      initial_tableau = input("Enter the tableau to move the card from (0-6)")
      initial_tableau= int(initial_tableau)
      final_tableau = input("Enter the tableau to move the card to (0-6) ")
      final_tableau = int(final_tableau)
        # if((initial_tableau != final_tableau) and initial_tableau ):

      action = ""
      self.tableau_to_tableau(initial_tableau, final_tableau, action)

    win = self.win()
    return(win)

  #########################################################################################################
  # Moves all the elements of the talon back to the stock
  # Add
  #########################################################################################################
  def talon_to_stock(self):
    while(len(self.talon) > 1):
      popped = self.talon.pop(-1)
      self.stock.append(popped)
    return (0)

  #########################################################################################################
  # card_color: what is the color of the card to check for alternating colors
  # Card_number: Make sure whether the card to be inserted into the tableau is less than the
  #              current card nubmer
  # Index: Index of the current in the talon. Used for removing from the stock/talon
  #########################################################################################################
  def tableau_addition(self,tableau_num):   #talon_to_tableau
    #add color checking feature   -- Maybe done
    #add number checking feature  -- Maybe done

    card = self.talon[-1]
    # tableau_num -= 1    # architecture change (0-6)
    if (len(self.tableau[tableau_num]) == 0):
      if(card[2] == 13):
        self.tableau[tableau_num].append(card)              #Adds the card to the tableau
        self.talon.pop(-1)
        return (self.return_scoring(1))

    top_tableau_card = self.tableau[tableau_num][-1]

    if(top_tableau_card[1] == card[1]):
      print("Operation not valid, Try Again")
      pdb.set_trace()
      pdb.set_trace()
    elif(top_tableau_card[2] <= card[2]):
      print("Operation not valid. Try Again")
      pdb.set_trace()
    elif((top_tableau_card[1] != card[1]) and (top_tableau_card[2]-1 == card[2])):
      self.tableau[tableau_num].append(card)              #Adds the card to the tableau
      self.talon.pop(-1)
      # self.scoring(1)
      return (self.return_scoring(1))
    else:
      print("Operation not possible")             #Removes the card
      pdb.set_trace()

      self.print_talon()
      self.print_tableua()


  def tableau_to_tableau (self, initial_tableau, final_tableau, action):
    try:
      if (action.find("to fd") != -1):  #tableau with multiple face-up cards, ex: 0id-1 to fd4
        init_tableau = int(action[0])
        final_tableau = int(action[-1])
        faceup_card = int(action[3]+action[4])
        if (len(self.tableau[final_tableau]) == 0):
          if (self.tableau[initial_tableau][faceup_card][2] == 13):
            counter = faceup_card
            for i in range(abs(faceup_card)):
              self.tableau[final_tableau].append(self.tableau[initial_tableau][counter])
              self.tableau[initial_tableau].pop(counter)
              counter += 1
            return (abs(faceup_card) * self.return_scoring(1))
            # if len(self.tableau[initial_tableau]) == 0:
            #   self.tableau[final_tableau][-1][3] = 1                # Marks the card as discovered              
            #   return (self.return_scoring(1))  # Bane of my existence - forgetting this line took me around 6 hours to debug
            # else: 
            #   self.tableau[initial_tableau][-1][3] = 1                # Marks the card as discovered
            #   self.tableau[final_tableau][-1][3] = 1                # Marks the card as discovered
            #   return (self.return_scoring(1))  # Bane of my existence - forgetting this line took me around 6 hours to debug
        elif((self.tableau[initial_tableau][faceup_card][1] != self.tableau[final_tableau][-1][1]) and (self.tableau[initial_tableau][faceup_card][2] == self.tableau[final_tableau][-1][2]-1)):
          counter = faceup_card
          for i in range(abs(faceup_card)):
            self.tableau[final_tableau].append(self.tableau[initial_tableau][counter])
            self.tableau[initial_tableau].pop(counter)
            counter += 1
          # if len(self.tableau[initial_tableau]) != 0:  # DO NOT USE, HAPPENS IN TAKE_ACTION
            # self.tableau[initial_tableau][-1][4] = 1                # Marks the card as discovered
          return (abs(faceup_card) * self.return_scoring(1))
        print("Error in tableau_to_tableau faceupcard part")
        pdb.set_trace()

      # self.tableau[initial_tableau][-1][3] = 1      # Remove
      elif (len(self.tableau[final_tableau]) == 0):
        if (self.tableau[initial_tableau][-1][2] == 13):
          self.tableau[final_tableau].append(self.tableau[initial_tableau][-1])              #Adds the card to the tableau
          self.tableau[initial_tableau].pop(-1)
          # if (self.tableau[final_tableau][-1][3] == 1):
            # return 0  # Reward for moving a card that has been moved in the tableau previously
          return (self.return_scoring(1))  # Bane of my existence - forgetting this line took me around 6 hours to debug
      elif((self.tableau[initial_tableau][-1][1] != self.tableau[final_tableau][-1][1]) and (self.tableau[initial_tableau][-1][2] == self.tableau[final_tableau][-1][2]-1)):
        self.tableau[final_tableau].append(self.tableau[initial_tableau][-1])
        self.tableau[initial_tableau].pop(-1)
        # self.scoring(1)        // No scores given for moving a card with the tableau
        # current_action = str(initial_tableau)+" "+str(final_tableau)+" "+str(self.tableau[initial_tableau][-1][0])+str(self.tableau[initial_tableau][-1][1])+str(self.tableau[initial_tableau][-1][2])+" "
        # current_action += str(self.tableau[final_tableau][-1][0])+str(self.tableau[final_tableau][-1][1])+str(self.tableau[final_tableau][-1][2])
        # pdb.set_trace()
        # for i in range (len(self.memoize)):
        #   if (self.memoize[i] == current_action):
        #     return 0  # Reward is 0 if same element is moved inside the tableau
        if (self.tableau[final_tableau][-1][3] == 1):
          return 0
        return (self.return_scoring(1))
      else:
        print("Operation not possible")             #Removes the card
        print(self.tableau[initial_tableau][-1])
        print(self.tableau[final_tableau][-1])
        pdb.set_trace()
        self.print_talon()
        self.print_tableua()
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print("error in take_action")
      print(action)
      pdb.set_trace()
  #########################################################################################################
  # card_pos: tableau number (automatically choses the top most card in the selected tableau)
  # pos: the foundation slot to insert the card into
  #########################################################################################################

  def tableau_to_foundation(self,card_pos,pos,action):
    try:
      card = self.tableau[card_pos][-1]             # card to be moved
      if(len(self.foundation[pos]) == 0):
        if(card[2] == 1):                           # Checks if card is an ACE
          self.foundation[pos].append(card)
          self.tableau[card_pos].pop(-1)
          # self.scoring(2)
          return (self.return_scoring(2))
        else:
          print("Operation not possible\n\n")
          pdb.set_trace()
      elif((self.foundation[pos][-1][2] == card[2]-1) and (self.foundation[pos][-1][0]) == card[0]):
        self.foundation[pos].append(card)
        self.tableau[card_pos].pop(-1)
        return (self.return_scoring(2))
      else:
        print("Operation not possible\n\n")
        pdb.set_trace()
    except:
      print("in tableau_to_foundation")
      pdb.set_trace()

  ########################################################################################################
  # pos: the foundation slot to insert the card into
  ########################################################################################################

  def talon_to_foundation(self,pos):
    card = self.talon[-1]
    if(len(self.foundation[pos]) == 0):
      if(card[2] == 1):
        self.foundation[pos].append(card)
        self.talon.pop(-1)
        return (self.return_scoring(2))
        # self.scoring(2)
      else:
        print("Operation not possible\n\n")
        pdb.set_trace()
    elif((self.foundation[pos][-1][2] == card[2]-1) and (self.foundation[pos][-1][0] == card[0])):           #CHANGED, MAYBE ERROR
      self.foundation[pos].append(card)
      self.talon.pop(-1)
      return (self.return_scoring(2))
    print("Operation not possible talon_to_foundation\n\n")
    pdb.set_trace()
      # self.scoring(2)


  def open_talon_to_foundation(self,foundation_num,talon_card_num):
    # print("INSIDE@")
    try:
      if (len(self.foundation[foundation_num]) == 0):
        if (self.open_talon[talon_card_num][2] == 1):
          self.foundation[foundation_num].append(self.open_talon[talon_card_num])
          self.open_talon.pop(talon_card_num)
          return (self.return_scoring(2))
        else:
          print("ERROR OPERATION FAILED, CHECK open_talon_to_foundation POLICIES")
          pdb.set_trace()
      elif((self.foundation[foundation_num][-1][2] == self.open_talon[talon_card_num][2]-1) and (self.foundation[foundation_num][-1][0] == self.open_talon[talon_card_num][0])):           #CHANGED, MAYBE
        self.foundation[foundation_num].append(self.open_talon[talon_card_num])
        self.open_talon.pop(talon_card_num)
        return self.return_scoring(2)
      else:
        print("open_talon_to_foundation failed")
        pdb.set_trace()
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print("Inside OPEN_TALON_TO_FOUNDATION")
      pdb.set_trace()

  def open_talon_to_tableau(self,talon_card,tableau_num):
    try:
      # print("INSIDE!")
      card = self.open_talon[talon_card]
      # tableau_num -= 1    # architecture change (0-6)
      if (len(self.tableau[tableau_num]) == 0):
        if(card[2] == 13):
          self.tableau[tableau_num].append(card)              #Adds the card to the tableau
          self.tableau[tableau_num][-1][3] = 1
          self.open_talon.pop(talon_card)                     # Marks the card as discovered
          return (self.return_scoring(1))

      top_tableau_card = self.tableau[tableau_num][-1]

      if(top_tableau_card[1] == card[1]):
        print("Operation not valid, Try Again")
        pdb.set_trace()
      elif(top_tableau_card[2] <= card[2]):
        print("Operation not valid. Try Again")
        pdb.set_trace()
      elif((top_tableau_card[1] != card[1]) and (top_tableau_card[2]-1 == card[2])):
        self.tableau[tableau_num].append(card)              #Adds the card to the tableau
        if len(self.tableau[tableau_num]) != 0:
          self.tableau[tableau_num][-1][4] = 1                # Marks the card as a faceup card
        self.open_talon.pop(talon_card)
        # self.scoring(1)
        return (self.return_scoring(1))
      else:
        print("Operation not possible")             #Removes the card
        pdb.set_trace()

        self.print_talon()
        self.print_tableua()
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      pdb.set_trace()

  #########################################################################################################
  #Parameters:-
  # num: Takes in the number of cards flipped in the turnstock process (starts from 0)
  #########################################################################################################

  def flip_stock(self):
    if(len(self.stock)>=1):
      self.talon.append(self.stock.pop())
      # self.talon.append(self.stock.pop())
      # self.talon.append(self.stock.pop())
      return (0)

    # elif(len(self.stock)>0 and len(self.stock)<3):
      # for i in range(len(self.stock)):
        # self.talon.append(self.stock.pop())
      # return (0)

    elif(len(self.stock) == 0):
      # pdb.set_trace()
      # if(self.stock_resets == 3):
      #   self.scoring(3);    # Will deduct points
      self.stock_resets += 1;
      for i in range(len(self.talon)):
        self.stock.append(self.talon.pop())
        # pdb.set_trace()
      if (self.stock_resets >= 3):
        self.stock_resets = 0
        return(self.return_scoring(3))
      else:
        return(0)

  #########################################################################################################
  # move types:
  # 1 - to tableau         or  5 points
  # 2 - to foundation      or  10 points
  # 3 - turn stock thrice  or -25 points
  #########################################################################################################

  def scoring(self,move_type):
    if(move_type == 1):
      self.score += 5;
    elif(move_type == 2):
      self.score += 10;
    elif(move_type == 3):
      self.score -= 25;
      if(self.score<0):
        self.score = 0;

  def return_scoring (self, move_type):
    if(move_type == 1):
      return(5)
    elif(move_type == 2):
      return 10
    elif(move_type == 3):
      return -25
      if (self.score - 25 > 0):
        return -25
      else:
        return (25-self.score)

  def UX_talon(self,card_num):
    output = ""
    card = self.talon[card_num]
    num = str(card[2])
    if(int(num)<10):
      num += " "
    if(card[2] == 1):
      num = "A "
    elif(card[2] == 11):
      num = "J "
    elif(card[2] == 12):
      num = "Q "
    elif(card[2] == 13):
      num = "K "
    output = card[0] + " " + card[1] + " " + num
    return output

  def print_talon(self):
    if(len(self.stock) != 0):
      print("\n\n                                     Talon:\n")
      print("|||||")
      print("|||||")
      print("|||||")
      print("|||||\n")
    output = ""
    print("\n\n\n")
    #len_talon = len(self.talon)
    if(len(self.talon) > 0):
      if(len(self.talon) > 3):
        loop = 1
        while(loop < 4):
          output = self.UX_talon((len(self.talon)-loop))
          print(output + "\n")
          loop += 1
      else:
        x = len(self.talon)
        while(x > 0):
          output = self.UX_talon(x-1)
          print(output + "\n")
          x -= 1
    print(self.open_talon)
    print(len(self.open_talon))


  def print_tableua(self):
    # i = len(self.tableau)
    i = 6
    maxx = 0
    print("\n\n                                     Tableau\n\n")
    for i in range(7):
      temp = len(self.tableau[i])
      if(temp>maxx):
        maxx = temp

    for i in range(maxx):   #safe bound 12
      counter = 0
      for j in range(7):
        if(i<len(self.tableau[j]) and (len(self.tableau[j])>0)):
          output = ""
          num = str(self.tableau[j][i][2])
          if(int(num)<10):
            num += " "
          if(self.tableau[j][i][2] == 1):
            num = "A "
          elif(self.tableau[j][i][2] == 11):
            num = "J "
          elif(self.tableau[j][i][2] == 12):
            num = "Q "
          elif(self.tableau[j][i][2] == 13):
            num = "K "
          output = self.tableau[j][i][0] + " " + self.tableau[j][i][1] + " " + num + " " + str(self.tableau[j][i][4]) + "  |  "
          print(output,end = "  ")
        elif(i>len(self.tableau[j])-1):
          counter += 1
          print("               ",end ="")
        if(counter == 7):
          break
      print("\n")
    print("\n")
    print(possible_actions)

    #def print_foundation(self):
      #for

  def print_foundation(self):
    print("\n                                       Foundation\n\n")
    for i in range(4):
      if(len(self.foundation[i]) > 0):
        # output = self.UX_foundation()         # FIX (error in UX_foundation())
        print(self.foundation[i])
        # print(output)
        print("            ")
      else:
        print("            ")


  def UX_foundation(self):
    output = ""
    card = self.foundation[-1]        # ERROR
    num = card[2]                 #experimental
    if(int(num)<10):
      num += " "
    if(card[2] == 1):
      num = "A "
    elif(card[2] == 11):
      num = "J "
    elif(card[2] == 12):
      num = "Q "
    elif(card[2] == 13):
      num = "K "
    output = card[0] + " " + card[1] + " " + num
    return output


  def UI(self):

    self.print_talon()
    self.print_tableua()
    # self.print_foundation()
    print (self.foundation)
    print ("Length of self.past_actions is", len(self.past_actions))


  def win(self):
    t_cards_foundation = 0
    for i in range(4):
      t_cards_foundation += len(self.foundation[i])

    if(t_cards_foundation == 52):
      self.return_game_state = 1
      print("Congratulations, you win")
      return(0)

    return(1)
      # ADD FUNCTIONALITY FOR ALERTING GAME OVER

  # This function eliminates the need for the stock
  def playable_stock(self):
    self.open_talon = self.stock
    # counter = 1
    # for i in range(len(self.stock)):
    #   if (counter%3 == 0):
    #     self.open_talon.append(self.stock[i])
    #     counter = 0
    #   counter += 1


  # Function for creating face up card actions
  def is_open_action(self,possible_actions):
    for i in range(7):  # Is the number of stacks in the tableau
      if (len(self.tableau[i]) != 0):
        j = len(self.tableau[i])-1
        while (j>=0):   # Counter for cycling face up cards
          if (self.tableau[i][j][4] == 1):    # checks if the card is a face up card
            card_stack = str(i) + "id" + str(j-len(self.tableau[i]))    # Format: 0id-1 to fd4  where 0=tableau_number, -1 is the card number in the tableau and 4 is the final tableau to move to
            for k in range(7):
              if (i == k): continue
              if (len(self.tableau[k]) >= 0):
                action = card_stack + " to fd" + str(k)
                legality = self.is_legal(action)
                if (legality == True and self.test_action(action) == True):
                  possible_actions.append(action)
            j -= 1
          else:
            break
    return possible_actions



  def is_legal(self, action):
    # pdb.set_trace()
    # if (len(self.open_talon) == 0):
      # print("Open talon length is 0")
      # pdb.set_trace()
    try:
      if (action.find("to fd") != -1):  #tableau with multiple face-up cards, ex: 0id-1 to fd4
        initial_tableau = int(action[0])
        final_tableau = int(action[-1])
        faceup_card = int(action[3]+action[4])
        if (len(self.tableau[initial_tableau]) == 0):
          return False
        if (len(self.tableau[final_tableau]) == 0):
          if(self.tableau[initial_tableau][faceup_card][2] == 13):
            return True
          else: return False
          # else: return False
        if(len(self.tableau[initial_tableau])<=0 and len(self.tableau[final_tableau])<=0):
          return False
        if((self.tableau[initial_tableau][faceup_card][1] != self.tableau[final_tableau][-1][1]) and (self.tableau[initial_tableau][faceup_card][2] == self.tableau[final_tableau][-1][2]-1)):
          return True
        else:
          return False

      # talon to tableau ex: t to ta1
      # elif((action.find("t to") != -1) and (action.find("ta") != -1)):  #talon to tableau
      #   if(len(self.open_talon) == 0):
      #     return False
      #   card = self.talon[-1]
      #   tableau_num = int(action[7])   # ex: t to ta6
      #   if (len(self.tableau[tableau_num]) == 0):
      #     if(self.talon[-1][2] == 13):
      #       return True
      #     else: return False
      #   length = self.tableau[tableau_num]                          #tableau_num denotes the tableau to insert cards in
      #   top_tableau_card = self.tableau[tableau_num][-1]
      #   if(top_tableau_card[1] == card[1]):
      #     return False
      #   elif(top_tableau_card[2] <= card[2]):
      #     return False
      #   elif((top_tableau_card[1] != card[1]) and (top_tableau_card[2]-1 == card[2])):
      #     return True
      #   else:
      #     return False

      # Flip stock or talon: fl
      elif (action.find("fl") != -1):
        if (len(self.stock)>0 or len(self.talon)>0):
          return True
        else: return False

      # talbeau to foundation ex: ta3 to f1
      elif ((action.find("to f") != -1) and (action.find("ta") != -1)):
        # if (action.find("to f")):  # ex: ta1 to f3
        if (len(self.tableau[int(action[2])])) == 0:
          return False
        pos = int(action[8])
        tableau_num = int(action[2])
        card = self.tableau[tableau_num][-1]  # ERROR: CHANGE FROM TALON TO TABLEAU, TALON HAS NO USE HERE
        if(len(self.foundation[pos]) == 0):
          if(card[2] == 1):                   # Checks if card is an ACE
            return True
          else:
            return False
        elif((self.foundation[pos][-1][2] == card[2]-1) and (self.foundation[pos][-1][0]) == card[0]):
          return True
        else:
          # print("Operation not possible\n\n")
          return False
      # open_talon to foundation
      elif (action.find("op_t") != -1 and action.find("to f") != -1):  # op_t5 to f4
        talon_number = None
        if (ord(action[5]) >= 48 and ord(action[5])<=57):
          talon_number = int(action[4]+action[5])
        else:
          talon_number = int(action[4])
        foundation_number = int(action[-1])
        if (len(self.foundation[foundation_number]) == 0):
          if (self.open_talon[talon_number][2] == 1):
            return True
          else:
            return False
        elif (self.foundation[foundation_number][-1][2] == self.open_talon[talon_number][2]-1 and self.foundation[foundation_number][-1][0] == self.open_talon[talon_number][0]):
          return True
        else:
          return False
      # talon to foundation ex: t to f1
      # elif((action.find("to f") != -1) and (action.find("t") != -1)):   #t to f3
      #   if(len(self.talon) == 0):
      #     return False
      #   pos = int (action[-1])
      #   card = self.talon[-1]
      #   if(len(self.foundation[pos]) == 0):
      #     if(card[2] == 1):
      #       return True
      #     else:
      #       return False
      #   elif((self.foundation[pos][-1][2] == card[2]-1) and (self.foundation[pos][-1][0] == card[0])):           #CHANGED, MAYBE ERROR
      #     return True

      # tableau to tableau ex: ta1 to ta3
      elif((action.find("ta") == 0) and (action.find("to ta") != -1) and len(self.tableau[int(action[2])])>0): #ex: ta2 to ta3
        final_tableau = int(action[9])
        initial_tableau = int(action[2])
        if (len(self.tableau[initial_tableau]) == 0):
          return False
        if (len(self.tableau[final_tableau]) == 0):
          if(self.tableau[initial_tableau][-1][2] == 13):
            return True
          else: return False
          # else: return False
        if(len(self.tableau[initial_tableau])<=0 and len(self.tableau[final_tableau])<=0):
          return False
        if((self.tableau[initial_tableau][-1][1] != self.tableau[final_tableau][-1][1]) and (self.tableau[initial_tableau][-1][2] == self.tableau[final_tableau][-1][2]-1)):
          return True
        else:
          # print("Operation not possible")             #Removes the card
          return False

      elif (action.find("op_t") != -1 and action.find("->tableau") != -1): #op_t6 ->tableau5
        if(len(self.open_talon) == 0):
          return False
        open_talon_card = None
        if (ord(action[5]) >= 48 and ord(action[5])<=57):
          open_talon_card = int(action[4]+action[5])
        else:
          open_talon_card = int(action[4])
        card = self.open_talon[open_talon_card]
        tableau_num = int(action[-1])   # ex: t to ta6
        if (len(self.tableau[tableau_num]) == 0):
          if(self.open_talon[open_talon_card][2] == 13):
            return True
          else: return False
        length = self.tableau[tableau_num]                          #tableau_num denotes the tableau to insert cards in
        top_tableau_card = self.tableau[tableau_num][-1]
        if(top_tableau_card[1] == card[1]):   # checks for cards being different colors
          return False
        elif(top_tableau_card[2] <= card[2]):
          return False
        elif((top_tableau_card[1] != card[1]) and (top_tableau_card[2]-1 == card[2])):
          return True
        else:
          return False
      else:
        return False
    # except:
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print("Error in is_legal")
      print (action)
      pdb.set_trace()
      # print (error)

  def return_score (self):
    return self.score

  def return_foundation(self):
    return(self.foundation)

  def return_talon(self):
    return(self.talon)

  def return_stock(self):
    return(self.stock)

  def return_tableau(self):
    return(self.tableau)

  def is_terminal(self):
    win_loose = self.win();
    if(win_loose == 0):
      return 1
    else: return 0


  def get_actions(self):
    possible_actions = []
    string_builder  = ""  # for debugging purposes
    try:
      possible_actions = []
      # pdb.set_trace()
      # string_builder = "fl"               #fl - flip the stock/talon
      # legality = self.is_legal(string_builder)
      # if (legality == True):
        # possible_actions.append(string_builder)
      for i in range(7):    # 7 is the number of tableaus
        string_builder = "t to ta" + str(i)   # t to ta1 - talon to tableau
        legality = self.is_legal(string_builder)
        if (legality == True):
          possible_actions.append(string_builder)
        for j in range(7):
          if (i!=j):
            string_builder = "ta" + str(i) + " to ta" + str(j)   # ta1 to ta2 - tabelau to tableau
            legality = self.is_legal(string_builder);
            if (legality == True and self.test_action(string_builder) == True):
              possible_actions.append(string_builder)
        for j in range(4):
          string_builder = "ta"+str(i)+" to f"+str(j)    # ta1 to f1 - tableau to foundation
          legality = self.is_legal(string_builder)
          if (legality == True):
            possible_actions.append(string_builder)
          string_builder = "t to f"+str(j)     # t to f1 - talon to foundation
          legality = self.is_legal(string_builder)
          if (legality == True):
            possible_actions.append(string_builder)
      for i in range(len(self.open_talon)):
        for j in range(4):
          string_builder = "op_t" + str(i) + " to f" + str(j)   # op_t9 to f3
          legality = self.is_legal(string_builder)
          if (legality == True):
            possible_actions.append(string_builder)
        for j in range(7):
          string_builder = "op_t" + str(i) + " ->tableau" + str(j)   # op_t9 to ta3
          # print(string_builder)
          legality = self.is_legal(string_builder)
          if (legality == True):
            possible_actions.append(string_builder)
      self.is_open_action(possible_actions)
      # if (len(possible_actions) == 0):
      #   print("possible_actions has 0 states")
      #   # pdb.set_trace()
      # else:
      #   print("Possible_actions has ", len(possible_actions))
      return possible_actions
      # return list(chain.from_iterable([func(self) for func in possible_actions]))  #generate actions and flatten lists   # known as single line functions for lists REFERENCE
      # pdb.set_trace()
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print("Error in get_actions")
      pdb.set_trace()

    return possible_actions


  def test_action (self,action):
    try:
      game_state = [self.open_talon,self.tableau,self.foundation]
      game_state[0] = copy.deepcopy(self.open_talon)
      game_state[1] = copy.deepcopy(self.tableau)
      game_state[2] = copy.deepcopy(self.foundation)
      past_actions = copy.deepcopy(self.past_actions)
      if (self.take_action(action) < 0):
        self.open_talon = game_state[0]
        self.tableau = game_state[1]
        self.foundation = game_state[2]
        self.past_actions = copy.deepcopy(past_actions)
        if (type(self.past_actions) == int):
          pdb.set_trace()
        return False
      self.open_talon = game_state[0]
      self.tableau = game_state[1]
      self.foundation = game_state[2]
      self.past_actions = copy.deepcopy(past_actions)
      if (type(self.past_actions) == int):
        pdb.set_trace()
      return True
    except:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print("Error in test_actions")
      pdb.set_trace()





  def take_action (self, action):
    try:
      # self.actions.append(action)
      # self.past_actions.append([self.open_talon,self.tableau,self.foundation])
      # print (action)

      #tableau with multiple face-up cards, ex: 0id-1 to fd4
      if (type(self.past_actions) == int):
        pdb.set_trace()
      if (action.find("to fd") != -1):
        reward = 0
        initial_tableau = int(action[0])
        final_tableau = int(action[-1])
        faceup_card = int(action[3]+action[4])
        self.tableau_to_tableau(initial_tableau, final_tableau, action)
        for i in range(7):
          if (len(self.tableau[i]) != 0 and self.tableau[i][-1][4] != 1):
            self.tableau[i][-1][4] = 1      # makes the last card a faceup card
            reward = 5
        temp = [self.open_talon,self.tableau,self.foundation]
        if (len(self.past_actions)>15):
          self.past_actions = self.past_actions[-14:]
        for i in range(len(self.past_actions)):
          if (temp == self.past_actions[i]):
            return (-15)
        self.past_actions.append([self.open_talon,self.tableau,self.foundation])
        return (reward)

      # involves flipping the stock or talon
      elif (action.find("fl") != -1):
        reward = self.flip_stock()
        return (reward)

       # is talon to tableau
      elif (action.find("t to ta") != -1):
        tableau_num = int(action[7])
        reward = self.tableau_addition(tableau_num)
        self.tableau[tableau_num][-1][4] = 1    # makes the last card a faceup card
        return (reward)

      # is tableau to tableau: ta1 to ta2
      elif (action.find("to ta") != -1):
        initial_tableau = int(action[2])
        final_tableau = int(action[9])
        reward = 0
        self.tableau_to_tableau(initial_tableau, final_tableau, action)
        for i in range(7):
          if (len(self.tableau[i]) != 0 and self.tableau[i][-1][4] != 1):
            self.tableau[i][-1][4] = 1        # Marks the card as a faceup card
            reward = 5
        temp = [self.open_talon,self.tableau,self.foundation]
        if (len(self.past_actions)>15):
          self.past_actions = self.past_actions[-14:]
        for i in range(len(self.past_actions)):
          if (temp == self.past_actions[i]):
            return (-15)
        self.past_actions.append([self.open_talon,self.tableau,self.foundation])
        return (reward)

      # is tableau to foundation: ta1 to f1
      elif (action.find("ta") != -1 and action.find("to f") != -1):
        tableau_num = int(action[2])
        foundation_num = int(action[8])
        reward = self.tableau_to_foundation(tableau_num,foundation_num,action)
        if (len(self.tableau[tableau_num]) != 0):
          self.tableau[tableau_num][-1][4] = 1

        self.past_actions = []
        return (reward)

      # elif (action.find("t to") != -1 and action.find("f") != -1):   #is talon to foundation: t to f1
      #   foundation_num = int(action[6])
      #   reward = self.talon_to_foundation(foundation_num)
      #   return (reward)

      # op_t5 to f4
      elif (action.find("op_t") != -1 and action.find("to f") != -1):
        foundation_num = int(action[-1])
        open_talon_num = None
        if (ord(action[5]) >= 48 and ord(action[5])<=57):
          open_talon_num = int(action[4]+action[5])
        else:
          open_talon_num = int(action[4])
        reward = self.open_talon_to_foundation(foundation_num, open_talon_num)
        self.past_actions = []
        return (reward)

      elif (action.find("op_t") != -1 and action.find("->tableau") != -1):
        open_talon_num = None
        if (ord(action[5]) >= 48 and ord(action[5])<=57):
          open_talon_num = int(action[4]+action[5])
        else:
          open_talon_num = int(action[4])
        tableau_num = int(action[-1])
        reward = self.open_talon_to_tableau(open_talon_num,tableau_num)
        self.tableau[tableau_num][-1][4] = 1     # Marks this as a faceup card
        self.past_actions = []
        return (reward)
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print("error in take_action")
      print(action)
      pdb.set_trace()



  def __copy__(self):
    Game = game()
    Game.stock = copy.deepcopy(self.stock)
    Game.foundation = copy.deepcopy(self.foundation)
    Game.talon = copy.deepcopy(self.talon)
    Game.tableau = copy.deepcopy(self.tableau)
    Game.score = self.score
    Game.stock_resets = self.stock_resets
    Game.cached_actions = copy.deepcopy(self.cached_actions)
    Game.last_action = copy.deepcopy(self.last_action)
    Game.actions = copy.deepcopy(self.actions)
    Game.open_talon = copy.deepcopy(self.open_talon)
    Game.return_game_state = copy.deepcopy(self.return_game_state)
    Game.second_last_action = self.second_last_action
    Game.past_actions = copy.deepcopy(self.past_actions)
    # game.
    return Game
    # board.cached_actions, board.last_action = self.cached_actions, self.last_action
    # board.verify_not_checked, board.allow_king_capture = self.verify_not_checked, self.allow_king_capture

  # def monte_carlo_tree_construction(self):


class game_states(game):
  def __init__(self):
    super().__init__()
    self.state = []
    self.black_listStates = []

  def add_state(self,obj):
    self.state.append(obj)

  def check_repetetive_state(self,obj):
    for elem in self.state:
      if obj == elem:
        break;
      else:
        self.state.append(obj)

def main():
  a = game()
  state = game_states()
  play = 1
  while(play == 1):
    # play = a.instructions()
    array = a.get_actions()
    print(str(array) + "\n" + str(len(array)))
    # pdb.set_trace()
    state.add_state(a)

# main()
"""
def take_action(self, action):
        # reward = self.current_state.move_piece(action)
    reward = self.current_state.
        # IMPLEMENT a call that actually moves stuff

        pdb.set_trace()
        self.current_state.last_action = action   # Setup functions for last_action  ERROR  // Global CHANGE of previous_player to previous_action
        # self.current_state.last_action, previous_state = action, self.current_player   # Setup functions for last_action  ERROR  // Global CHANGE of previous_player to previous_action
        # self.update_current_player()                # Can be found in abstract_state.py  # not needed as solitaire is a single player game

        self.current_state.cached_actions = []
        self.get_actions()  # Line 53
        fetch_reward = self.get_reward(action)
        if (len(self.current_state.cached_actions) == 0):
          self.game_outcome = 'win' if self.current_state.return_game_state else 'in progress'
          # if self.game_outcome == 'win':
            # print("Game over")
        return
        # if self.current_state.return_game_state == 1:
            # self.game_outcome = previous_player if self.current_state.is_checked(self.get_current_color()) else 'draw'

        # The current player gets the opposite of the reward (e.g. losing a piece)
        return np.array([-1 * reward if player_idx == self.current_player else reward
                         for player_idx in range(self.num_players)])
"""

#Files to investigate


# File "../dealers/native_dealer.py", line 182, in run_trial
#     action_to_take = self.agents[current_state.current_player].select_action(current_state)
#   File "../agents/frameworks/recursive_bandit_framework.py", line 26, in select_action
#     return self.estimateV(state, self.depth)[1]  # return the best action
#   File "../agents/frameworks/recursive_bandit_framework.py", line 55, in estimateV
#     arm_data = self.run_pull(state, bandit, depth)
#   File "../agents/frameworks/recursive_bandit_framework.py", line 75, in run_pull
#     future_reward = self.estimateV(current_state, depth - 1)[0]  # [0] references the q_values for best action
#   File "../agents/frameworks/recursive_bandit_framework.py", line 34, in estimateV
#     return self.evaluation.evaluate(state), None  # no more depth, so default to the evaluation fn
#   File "../agents/evaluations/rollout_evaluation.py", line 19, in evaluate
#     total_rewards += self.run_rollout(state)
#   File "../agents/evaluations/rollout_evaluation.py", line 32, in run_rollout
#     rewards += sim_state.take_action(action)
#   File "../dealers/simulators/chess.py", line 39, in take_action
#     self.current_state.last_action, previous_player = action, self.current_player
#   File "../dealers/simulators/chess.py", line 39, in take_action
#     self.current_state.last_action, previous_player = action, self.current_player
#   File "/usr/lib/python3.6/bdb.py", line 51, in trace_dispatch
#     return self.dispatch_line(frame)
#   File "/usr/lib/python3.6/bdb.py", line 70, in dispatch_line
#     if self.quitting: raise BdbQuit