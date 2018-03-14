import random
import math
import pdb


# Testing for the foundation to tableau function          
# Imporve UI
# Integrate with Alex's codes


class game:
  def __init__(self):
    #self.cards = {'K':[['B','S'],['B','C'],['R','D'],['R','D']],"Q":[['B','S'],['B','C'],['R','D'],['R','D']],"J":[['B','S'],['B','C'],['R','D'],['R','D']],"A":[['B','S'],['B','C'],['R','D'],['R','D']],"2":[['B','S'],['B','C'],['R','D'],['R','D']],"3":[['B','S'],['B','C'],['R','D'],['R','D']]}
    #self.cards.update({"4":[['B','S'],['B','C'],['R','D'],['R','D']],"5":[['B','S'],['B','C'],['R','D'],['R','D']],"6":[['B','S'],['B','C'],['R','D'],['R','D']],"7":[['B','S'],['B','C'],['R','D'],['R','D']],"8":[['B','S'],['B','C'],['R','D'],['R','D']],"9":[['B','S'],['B','C'],['R','D'],['R','D']],"10":[['B','S'],['B','C'],['R','D'],['R','D']]})
    #self.cards.update({"A":[['B','S'],['B','C'],['R','D'],['R','D']]})
    self.cards = []     # NOT USED, REMOVE
    self.tcards = []    # NOT USED PRESENTLY, JUST HOLDS A COPY OF EVERYTHING
    self.stock = []                             # Contains the decked to be flipped
    self.foundation = [[],[],[],[]]
    self.talon = []                            # Contains flipped cards
    self.tableau = [[],[],[],[],[],[],[]]       # 7 cards laid out aside eachother
    self.shuffle()
  
  def shuffle(self):

    n = []    
    for i in range(1,11):
      n.append(['D','R',i])
      n.append(['H','R',i])
      n.append(['S','B',i])
      n.append(['C','B',i])

    #n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n10 = [[1,'C','B'],[1,'D','R'],[1,'H','R'],[1,'S','B']]    #[[1,'c',b']] where 1 = no. of cards in the deck, c = club, b = black
    face_cards = ["K","Q","K","A"]
    for i in range(11,14):
      n.append(['C','B',i])
      # n.append(['C','B',""+face_cards[i-10]])   1 - A, 11 - J, 12 - Q, 13 - K
      n.append(['S','B',i])
      n.append(['D','R',i])
      n.append(['H','R',i])

    #for i in range(1,26):
    self.cards = n
    self.tcards = n
    self.assign_tableau(n)
  
    self.create_stock()

    #insert code
  
#########################################################################################################
# Name: assign_tableau
# Use: Used for filling up the tableau
# Paramterers: the list with all card combinations
#########################################################################################################  
  def assign_tableau(self,n):
    tableau_num = 0 
    for i in range(0,28):      # For each tableau
      x = random.randint(0,len(n)-1)   # Contains the card number
      #print("x is " + str(x) + " len of x  is " + str(len(n)) + "\n")
      card = n[x]                    # Stores a copy of the card
      if(len(self.tableau[tableau_num]) < tableau_num+1):
        self.tableau[tableau_num].append(card)
        if(len(self.tableau[tableau_num]) == tableau_num+1):
          tableau_num += 1
      
      n.pop(x)

    self.cards = n

  def create_stock(self):
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
    if(len(self.stock) or (self.talon)>0):
      print("1 to Flip the stock")                                            # Function Created

    if(len(self.talon)>0):
      print("2 to move a card from the talon to the tableau")              # Function Created 
    
    print("3 to move a card from the tableau to the foundation")             # Created but not checked
    print("4 to move a card from the talon to the foundation")
    if(len(self.stock)<3):
      print("Press 4 to flip all the cards from talon back to stock")         # Function Created

    choice = input("Choice ")
    choice = int(choice)
    if(choice == 1):
      self.flip_stock()
      #print UI stuff
    elif(choice == 2):
      tableau_num = input("Enter the tableau number to move to ")
      tableau_num = int(tableau_num)
      res = self.tableau_addition(tableau_num)
      if(res == 0):
        print("Operation not possible") 
      elif(res == 1):
        #Print UI
        self.UI()
    elif(choice ==3):
        foundation_num = input("Enter the foundation to move the card to (1-4) ")
        foundation_num = int(tableau_num)
        tableau_num = input("Enter the tableau to move the card from (1-7)")
        tableau_to_foundation(tableau_num-1,foundation_num-1)
    elif(choice ==4):
        self.talon_to_stock()
        
    return(1)

#########################################################################################################  
# Moves all the elements of the talon back to the stock
# Add 
#########################################################################################################  
  def talon_to_stock(self):
    while(len(self.talon) > 1):
      popped = self.talon.pop(-1)
      self.stock.append(popped)
    
#########################################################################################################  
#            card_color: what is the color of the card to check for alternating colors
#            Card_number: Make sure whether the card to be inserted into the tableau is less than the 
#                         current card nubmer
#            Index: Index of the current in the talon. Used for removing from the stock/talon
#########################################################################################################  
  def tableau_addition(self,tableau_num):                                                                 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!FICIFIXFIXFIXFIXFIX!!!!!!!!!!!
    #add color checking feature
    #add number checking feature
    #document code
    
    card = self.talon[-1]
    tableau_num -= 1
    length = self.tableau[tableau_num]                          #tableau_num denotes the tableau to insert cards in
    top_tableau_card = self.tableau[tableau_num][-1]
    
    if(top_tableau_card[1] == card[1]):
      print("Operation not valid, Try Again")
      return False
    elif(top_tableau_card[2] <= card[2]):
      print("Operation not valid. Try Again")
      return False
    elif((top_tableau_card[1] != card[1]) and (top_tableau_card[2]-1 == card[2])):
      self.tableau[tableau_num].append(card)              #Adds the card to the tableau
      self.talon.pop(-1)                  
    else:
      print("Operation not possible")             #Removes the card
      
      self.print_talon()
      self.print_tableua()
      return True

    # length = self.tableau[slot_num]
    # tableau_card = self.tableau[slot_num][length-1]             #Card on the top of the selected tableau
    # if(tableau_card[1] == card[1]):
    #   return False

    # elif(tableau_card[2] < card[2]):
    #   return False

    # else:
    #   self.tableau[slot_num].append(card)
    #   self.talon.pop(index)

#########################################################################################################  
#Parameters:-
# num: Takes in the number of cards flipped in the turnstock process (starts from 0)
#########################################################################################################  

  def flip_stock(self):
    
    if(len(self.stock)>=3):
      self.talon.append(self.stock.pop())
      self.talon.append(self.stock.pop())
      self.talon.append(self.stock.pop())

    elif(len(self.stock)>0 and len(self.stock)<3):
      for i in range(len(self.stock)):
        self.talon.append(self.stock.pop())

    elif(len(self.stock) == 0):
      for i in range(len(self.talon)):
        self.stock.append(self.talon.pop())
    
  def print_talon(self):
    print("\n\nTalon: \n")
    print("|||||")
    print("|||||")
    print("|||||")
    print("|||||\n")
    #len_talon = len(self.talon)
    if(len(self.talon) > 0):
      if(len(self.talon) > 3):
        print(self.talon[len(self.talon)-3])
        print(self.talon[len(self.talon)-2])
        print(self.talon[len(self.talon)-1])
      else:
        for i in range(len(self.talon)):
          print(self.talon[i])


  def print_tableua(self):
    i = len(self.tableau)
    max = 0
    print("\n\nTableau\n\n")
    for i in range(7):
      temp = len(self.tableau[i])
      if(temp>max):
        max = temp  

    for i in range(max):   #safe bound 12
      counter = 0
      for j in range(7):
        if(i<len(self.tableau[j]) and (len(self.tableau[i])>0)):
          output = ""
          num = str(self.tableau[j][i][2])
          if(int(num)<10):
            num += " "
          if(self.tableau[j][i][2] == 1):
            num = "A "
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
#########################################################################################################  
# card_pos: tableau number (automatically choses the top most card in the selected tableau)
# pos: the foundation slot to insert the card into
#########################################################################################################  

  def tableau_to_foundation(self,card_pos,pos):
    card = self.tableau[card_pos][-1]             # card to be moved
    if(len(self.foundation[pos]) == 0):
      if(card[2] == 1):    
        self.foundation[pos].append(card)
        self.tableau[card_pos].pop(-1)
      else:
        print("Operation not possuble\n\n")        
    elif(self.foundation[pos][-1][2] == card[2]-1):
      self.foundation[pos].append(card)
      self.tableau[card_pos].pop(-1)
    else:
      print("Operation not possuble\n\n")

########################################################################################################  
# pos: the foundation slot to insert the card into
########################################################################################################  

  def talon_to_foundation(self,pos):
    card = self.talon[-1]
    if(len(self.foundation[pos]) == 0):
      if(card[2] == 1):
        self.foundation[pos].append(card)
        self.talon.pop(-1)
      else:
        print("Operation not possuble\n\n")
    elif(self.foundation[pos][2] == card[2]-1):
      self.foundation[pos].append(card)
      self.talon.pop(-1)      

  def UI(self):
        
    self.print_talon()
    self.print_tableua()
    
  def win(self):
    t_cards_foundation = 0
    for i in range(4):
      t_cards_foundation += len(self.foundation[i])
    
    if(t_cards_foundation == 52):
      print("Congratulations, you win")
      # ADD FUNCTIONALITY FOR ALERTING GAME OVER
    
    

class game_states(game):
  def __init__(self):
    super().__init__()
    self.stage = []

  def add_state(self,obj):
    self.stage.append(obj)

def main():
  a = game()
  state = game_states()
  play = 1
  while(play == 1):
    play = a.instructions()
    state.add_state(a)

main()

