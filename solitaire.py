import random
import math
import pdb

class game:
  def __init__(self):
    #self.cards = {'K':[['B','S'],['B','C'],['R','D'],['R','D']],"Q":[['B','S'],['B','C'],['R','D'],['R','D']],"J":[['B','S'],['B','C'],['R','D'],['R','D']],"A":[['B','S'],['B','C'],['R','D'],['R','D']],"2":[['B','S'],['B','C'],['R','D'],['R','D']],"3":[['B','S'],['B','C'],['R','D'],['R','D']]}
    #self.cards.update({"4":[['B','S'],['B','C'],['R','D'],['R','D']],"5":[['B','S'],['B','C'],['R','D'],['R','D']],"6":[['B','S'],['B','C'],['R','D'],['R','D']],"7":[['B','S'],['B','C'],['R','D'],['R','D']],"8":[['B','S'],['B','C'],['R','D'],['R','D']],"9":[['B','S'],['B','C'],['R','D'],['R','D']],"10":[['B','S'],['B','C'],['R','D'],['R','D']]})
    #self.cards.update({"A":[['B','S'],['B','C'],['R','D'],['R','D']]})
    self.cards = []     # 
    self.tcards = []    # NOT USED PRESENTLY, JUST HOLDS A COPY OF EVERYTHING
    self.stock = []                             # Contains the decked to be flipped
    self.foundation = {}
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
    for i in range(0,24):
      #pdb.set_trace()
      x = random.randint(0,len(self.cards)-1)
      self.stock.append(self.cards[x])
      self.cards.pop(x)

#########################################################################################################
# Prints the instructions
#########################################################################################################

  def instructions(self):
    inp = -1
    self.UI()
    if(len(self.stock) or (self.talon)>0):
      print("1 to Flip the stock")  

    if(len(self.talon)>0):
      print("2 to move a card from the talon to the foundation or tableau")
    
    print("3 to move a card from the foundation to the tableau ")

    choice = input("Choice ")
    choice = int(choice)
    if(choice == 1):
      self.flip_stock()
      #print UI stuff
    elif(choice == 2):
      tableau_num = input("Enter the tableau number to move to ")
      res = self.tableau_addition(tableau_num)
      if(res == 0):
        print("Operation not possible")
      elif(res == 1):
        #Print UI
        self.UI()
    return(1)



  #def play(self):
    
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
    elif(top_tableau_card[2] >= card[2]):
      print("Operation not valid. Try Again")
      return False
    elif((top_tableau_card[1] == card[1]) and (top_tableau_card[2] < card[2])):
      self.tableau[tableau_num].append(card)              #Adds the card to the tableau
      self.talon.pop(-1)                               #Removes the card
      
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
    
    print("SNVDJ")
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
    print("|||||")
    print("|||||")
    print("|||||")
    print("|||||")
    len_talon = len(self.talon)
    if(len_talon > 0):
      if(len_talon > 3):
        print(self.talon[len_talon-3])
        print(self.talon[len_talon-2])
        print(self.talon[len_talon-1])
      else:
        for i in range(len_talon):
          print(self.talon[i])


  def print_tableua(self):
    len_tableau = len(self.tableau)
    i = len(self.tableau)
    
    for i in range(12):   #safe bound 12
      counter = 0
      for j in range(7):
        if(i<len(self.tableau[j]) and (len(self.tableau[i])>0)):
          print(self.tableau[j][i],end = "  ")
        elif(i>len(self.tableau[j])-1):
          counter += 1
          print("               ",end ="")
        if(counter == 7):
          break

      print("\n")

    #for i in range(len_tableau):
    #  for j in range(len(self.tableau[i])):
    #    if(len(self.tableau[i][j]) == 0):
    #      print("     ")
    #    print(self.tableau[i][j],end = "   ")
    #    print("\n")
    #print("\n\n")

  def UI(self):
        
    #self.print_talon()
    self.print_tableua()
    
    
def main():
  a = game()
  play = 1
  while(play == 1):
    play = a.instructions()

main()

