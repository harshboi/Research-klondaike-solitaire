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
    for i in range(0,9):
      n.append(['D','R',i+2])
      n.append(['H','R',i+2])
      n.append(['S','B',i+2])
      n.append(['C','B',i+2])
    #n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n10 = [[1,'C','B'],[1,'D','R'],[1,'H','R'],[1,'S','B']]    #[[1,'c',b']] where 1 = no. of cards in the deck, c = club, b = black
    face_cards = ["K","Q","K","A"]
    for i in range(10,14):
      n.append(['C','B',i-10])
      # n.append(['C','B',""+face_cards[i-10]])
      n.append(['S','B',i-10])
      n.append(['D','R',i-10])
      n.append(['H','R',i-10])
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

  def instructions(self):
    if(len(self.stock) or (self.talon)>0):
      print("Flip the stock")  
    if(len(self.talon)>0):
      print("Do you want to move a card from the talon")

  #def play(self):
    
#########################################################################################################  
#Parameters: slot_num: Which slot in the tableau should the card be inserted into
#            card_color: what is the color of the card to check for alternating colors
#            Card_number: Make sure whether the card to be inserted into the tableau is less than the 
#                         current card nubmer
#            Index: Index of the current in the talon. Used for removing from the stock/talon
#########################################################################################################  
  def check_tableau_addition(self,card,slot_num,index):
    len = self.tableau[slot_num]
    tableau_card = self.tableau[slot_num][len-1]  #Card on the top of the selected tableau
    if(tableau_card[1] == card[1]):
      return False
    elif(tableau_card[2] < card[2]):
      return False
    else:
      self.tableau[slot_num].append(card)
      self.talon.pop(index)

#########################################################################################################  
#Parameters:-
# num: Takes in the number of cards flipped in the turnstock process (starts from 0)
#########################################################################################################  

  def flip_stock(self,num):
    num += 1

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
    

def main():
  a = game()

main()

