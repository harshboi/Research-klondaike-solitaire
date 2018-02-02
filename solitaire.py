import random
import math

class game:
  def __init__(self):
    #self.cards = {'K':[['B','S'],['B','C'],['R','D'],['R','D']],"Q":[['B','S'],['B','C'],['R','D'],['R','D']],"J":[['B','S'],['B','C'],['R','D'],['R','D']],"A":[['B','S'],['B','C'],['R','D'],['R','D']],"2":[['B','S'],['B','C'],['R','D'],['R','D']],"3":[['B','S'],['B','C'],['R','D'],['R','D']]}
    #self.cards.update({"4":[['B','S'],['B','C'],['R','D'],['R','D']],"5":[['B','S'],['B','C'],['R','D'],['R','D']],"6":[['B','S'],['B','C'],['R','D'],['R','D']],"7":[['B','S'],['B','C'],['R','D'],['R','D']],"8":[['B','S'],['B','C'],['R','D'],['R','D']],"9":[['B','S'],['B','C'],['R','D'],['R','D']],"10":[['B','S'],['B','C'],['R','D'],['R','D']]})
    #self.cards.update({"A":[['B','S'],['B','C'],['R','D'],['R','D']]})
    self.cards = []
    self.tcards = []
    self.turnstock = {}
    self.foundation = {}
    self.talon = {}
    self.tableau = [[],[],[],[],[],[],[]]
  
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
      n.append(['C','B',face_cards[i-10]])
      n.append(['S','B',face_cards[i-10]])
      n.append(['D','R',face_cards[i-10]])
      n.append(['H','R',face_cards[i-10]])
    #for i in range(1,26):
    self.cards = n
    self.tcards = n
    assign_tableau(n)

    #insert code
  
#########################################################################################################
# Name: assign_tableau
# Use: Used for filling up the tableau
# Paramterers: the list with all card combinations
#########################################################################################################  
  def assign_tableau(self,n):
    tableau_num = 0 
    
    for i in range(0,28):      # For each tableau
      x = random.randint(0,len(n))   # Contains the card number
      card = n[x]                    # Stores a copy of the card
      if(len(self.tableau(tableau_num)) < tableau_num+1):
        self.tableau(tableau_num).append(card)
        if(len(self.tableau(tableau_num)) == tableau_num+1)
          tableau_num++
      n.pop(x)
    self.cards = n

#########################################################################################################
# Name: Used to add a card to the tabeau's seven card layer
# Use: Checks whether each stack has the correct number of cards and then adds to the tableau
# Parameters:
#########################################################################################################
  def append_tableau(self,value,tableau_num):
    
    for i in range(0,7):
      x = len(self.tableau[i])
    
      if x < (i+1):
        self.tabeau[i][x].append(value)
        break;


  #def error_handling(self,n):
    


  #def display_talon(self):
    #

  #def display_foundations(self):
    #insert code
  
  #def display_stock(self):
    #insert code

  #def display_tableau(self):
    #insert code

  #def legal_move_turnstock(self):
    #insert code

def main():
  a = game()
  print(a.cards.keys())

main()