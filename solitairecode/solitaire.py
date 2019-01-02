import random
import math
import pdb
from itertools import chain
import copy
import time

global str

# Work on is open function -- Function for moving multiple face up cards
# Add a function for moving multiple cards -- Multiple faceup cards at the same time (specifying the action)
# Reducing complexity by removing memoize and adding an extra dimension for storage in the array
# self.talon has a card that self.foundation does, check distribution of cards -- Done - Resolved
# Errors below have all been fixed
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
# TypeError: ufunc 'add' output (typecode 'O') could not be coerced to provided output parameter (typecode 'd') according to the casting rule ''same_kind''
# 100% (1 of 1) |##########################| Elapsed Time: 0:00:00 Time:  0:00:00


  # len(self.stock) = 45 ?? should be 24
  # commented line 194 in native_dealer.py
  # Line 427 error
    #   File "../dealers/simulators/solitairecode/solitaire.py", line 427, in is_legal
    #     top_tableau_card = self.tableau[tableau_num][-1]
    # IndexError: list index out of range
  # code handle it
  # Integrate with Alex's codes

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
      self.memoize = []
      self.actions = []
      self.second_last_action = None    # Is used for checking the second last card moved to prevent loops caused by repeating actions

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
  def tableau_addition(self,tableau_num):   #talon_to_tableau                                                              # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!FICIFIXFIXFIXFIXFIX!!!!!!!!!!!
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
    # initial_tableau -=1
    # final_tableau -= 1
    # memoize array structure = init_tableau fin_tableau init_card final_card
    # ex: '0 2 HR3 SB2'
    self.tableau[initial_tableau][-1][3] = 1
    if (len(self.tableau[final_tableau]) == 0):
      if (self.tableau[initial_tableau][-1][2] == 13):
        self.tableau[final_tableau].append(self.tableau[initial_tableau][-1])              #Adds the card to the tableau
        self.tableau[initial_tableau].pop(-1)
        if (self.tableau[final_tableau][-1][3] == 1):
          return 0  # Reward for moving a card that has been moved in the tableau previously
        return (self.return_scoring(1))  # Bane of my existence - forgetting this line took me around 6 hours to debug
    elif((self.tableau[initial_tableau][-1][1] != self.tableau[final_tableau][-1][1]) and (self.tableau[initial_tableau][-1][2] == self.tableau[final_tableau][-1][2]-1)):
      # self.memoize.append(str(final_tableau)+" "+str(initial_tableau)+" "+str(self.tableau[final_tableau][-1][0])+str(self.tableau[final_tableau][-1][1])+str(self.tableau[final_tableau][-1][2])+" ")
      # self.memoize[-1] += str(self.tableau[initial_tableau][-1][0])+str(self.tableau[initial_tableau][-1][1])+str(self.tableau[initial_tableau][-1][2])
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
          pdb.set_trace()
          print("Operation not possible\n\n")
      elif((self.foundation[pos][-1][2] == card[2]-1) and (self.foundation[pos][-1][0]) == card[0]):
        self.foundation[pos].append(card)
        self.tableau[card_pos].pop(-1)
        return (self.return_scoring(2))
      else:
        pdb.set_trace()
        print("Operation not possible\n\n")
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
    elif((self.foundation[pos][-1][2] == card[2]-1) and (self.foundation[pos][-1][0] == card[0])):           #CHANGED, MAYBE ERROR
      self.foundation[pos].append(card)
      self.talon.pop(-1)
      return (self.return_scoring(2))
      # self.scoring(2)

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
          output = self.tableau[j][i][0] + " " + self.tableau[j][i][1] + " " + num + "  |  "
          print(output,end = "  ")
        elif(i>len(self.tableau[j])-1):
          counter += 1
          print("             ",end ="")
        if(counter == 7):
          break
      print("\n")
    print("\n")

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


  def win(self):
    t_cards_foundation = 0
    for i in range(4):
      t_cards_foundation += len(self.foundation[i])

    if(t_cards_foundation == 52):
      print("Congratulations, you win")
      return(0)

    return(1)
      # ADD FUNCTIONALITY FOR ALERTING GAME OVER

  # Function for creating face up card actions
  def is_open_action(self,possible_actions):
    for i in range(7):  # Is the number of stacks in the tableau
      if (len(self.tableau[i]) != 0):
        j = len(self.tableau[i])-1
        while (j>=0):   # Counter for cycling face up cards
          if (self.tableau[i][j][4] == 1):    # checks if the card is a face up card
            card_stack = str(i) + "id" + str(j-len(self.tableau[i]))    # Format: 0id-1 to fd4  where 0=tableau_number, -1 is the card number in the tableau and 4 is the final tableau to move to
            for k in range(7):
              if (i == k):
                continue
              if (len(self.tableau[k]) > 0):
                action = card_stack + " to fd" + str(k)
                possible_actions.append(action)
            j -= 1
          else:
            break



  def is_legal(self, action):
    # pdb.set_trace()
    # talon to tableau ex: t to ta1
    try:
      if((action.find("t to") != -1) and (action.find("ta") != -1)):  #talon to tableau
        if(len(self.talon) == 0):
          return False
        card = self.talon[-1]
        tableau_num = int(action[7])   # ex: t to ta6
        if (len(self.tableau[tableau_num]) == 0):
          if(self.talon[-1][2] == 13):
            return True
          else: return False
        length = self.tableau[tableau_num]                          #tableau_num denotes the tableau to insert cards in
        top_tableau_card = self.tableau[tableau_num][-1]
        if(top_tableau_card[1] == card[1]):
          return False
        elif(top_tableau_card[2] <= card[2]):
          return False
        elif((top_tableau_card[1] != card[1]) and (top_tableau_card[2]-1 == card[2])):
          return True
        else:
          return False

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
            # print("Operation not possible\n\n")
            return False
        elif((self.foundation[pos][-1][2] == card[2]-1) and (self.foundation[pos][-1][0]) == card[0]):
          return True
        else:
          # print("Operation not possible\n\n")
          return False

      # talon to foundation ex: t to f1
      elif((action.find("to f") != -1) and (action.find("t") != -1)):   #t to f3
        if(len(self.talon) == 0):
          return False
        pos = int (action[-1]);
        card = self.talon[-1]
        if(len(self.foundation[pos]) == 0):
          if(card[2] == 1):
            return True;
            # self.foundation[pos].append(card)
            # self.talon.pop(-1)
            # self.scoring(2)
          else:
            return False
        elif((self.foundation[pos][-1][2] == card[2]-1) and (self.foundation[pos][-1][0] == card[0])):           #CHANGED, MAYBE ERROR
          return False;
          # self.foundation[pos].append(card)
          # self.talon.pop(-1)
          # self.scoring(2)

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

      else:
        return False
    # except:
    except AssertionError as error:
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
    # pdb.set_trace()
    string_builder = "fl"               #fl - flip the stock/talon
    legality = self.is_legal(string_builder)
    if (legality == True):
      possible_actions.append(string_builder)
    for i in range(7):    # 7 is the number of tableaus
      string_builder = "t to ta" + str(i)   # t to ta1 - talon to tableau
      legality = self.is_legal(string_builder)
      if (legality == True):
        possible_actions.append(string_builder)
      for j in range(7):
        if (i!=j):
          string_builder = "ta" + str(i) + " to ta" + str(j)   # ta1 to ta2 - tabelau to tableau
          legality = self.is_legal(string_builder);
          if (legality == True):
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
    self.is_open_action(possible_actions)
    # return list(chain.from_iterable([func(self) for func in possible_actions]))  #generate actions and flatten lists   # known as single line functions for lists REFERENCE
    # pdb.set_trace()
    return possible_actions

  def take_action (self, action):
    self.actions.append(action)
    if (action.find("fl") != -1):  # involves flipping the stock or talon
      reward = self.flip_stock()
      return (reward)
    elif (action.find("t to ta") != -1):  # is talon to tableau
      tableau_num = int(action[7])
      reward = self.tableau_addition(tableau_num)
      return (reward)
    elif (action.find("to ta") != -1):   # is tableau to tableau: ta1 to ta2
      initial_tableau = int(action[2])
      final_tableau = int(action[9])
      reward = self.tableau_to_tableau(initial_tableau, final_tableau, action)
      for i in range(7):
        if (len(self.tableau[i]) != 0):
          self.tableau[i][-1][4] = 1
      return (reward)
    elif (action.find("ta") != -1 and action.find("to f") != -1):  # is tableau to foundation: ta1 to f1
      tableau_num = int(action[2])
      foundation_num = int(action[8])
      reward = self.tableau_to_foundation(tableau_num,foundation_num,action)
      return (reward)
    elif (action.find("t to") != -1 and action.find("f") != -1):   #is talon to foundation: t to f1
      foundation_num = int(action[6])
      reward = self.talon_to_foundation(foundation_num)
      return (reward)

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
    # game.
    return Game
    # board.cached_actions, board.last_action = self.cached_actions, self.last_action
    # board.verify_not_checked, board.allow_king_capture = self.verify_not_checked, self.allow_king_capture

  def monte_carlo_tree_construction(self):


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
