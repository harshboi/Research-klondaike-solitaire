import random
import math

class game:
  def __init__(self):
    self.cards = {'K':[['B','S'],['B','C'],['R','D'],['R','D']],"Q":[['B','S'],['B','C'],['R','D'],['R','D']],"J":[['B','S'],['B','C'],['R','D'],['R','D']],"A":[['B','S'],['B','C'],['R','D'],['R','D']],"2":[['B','S'],['B','C'],['R','D'],['R','D']],"3":[['B','S'],['B','C'],['R','D'],['R','D']]}
    self.cards.update({"4":[['B','S'],['B','C'],['R','D'],['R','D']],"5":[['B','S'],['B','C'],['R','D'],['R','D']],"6":[['B','S'],['B','C'],['R','D'],['R','D']],"7":[['B','S'],['B','C'],['R','D'],['R','D']],"8":[['B','S'],['B','C'],['R','D'],['R','D']],"9":[['B','S'],['B','C'],['R','D'],['R','D']],"10":[['B','S'],['B','C'],['R','D'],['R','D']]})
    self.cards.update({"A":[['B','S'],['B','C'],['R','D'],['R','D']]})
    self.turnstock = {}
    self.foundation = {}
    self.talon = {}
    self.tableau = [[],[],[],[],[],[],[]]
  
  def shuffle(self):
    #11 = K, 12 = Q, 13 = J, 14 = A
    n[0] = n[1] = []    
    for i in range(2,10):
      n[i] = [[1,'C','B',i],[1,'D','R',i],[1,'H','R',i],[1,'S','B',i]]
    #n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n10 = [[1,'C','B'],[1,'D','R'],[1,'H','R'],[1,'S','B']]    #[[1,'c',b']] where 1 = no. of cards in the deck, c = club, b = black
    n[11] = [[1,'C','B',"K"],[1,'S','B',"K"],[1,'D','R',"K"],[1,'H','R',"K"]]
    n[12] = [[1,'C','B',"Q"],[1,'S','B',"Q"],[1,'D','R',"Q"],[1,'H','R',"Q"]]
    n[13] = [[1,'C','B',"J"],[1,'S','B',"J"],[1,'D','R',"J"],[1,'H','R',"J"]]
    n[14] = [[1,'C','B',"A"],[1,'S','B',"A"],[1,'D','R',"A"],[1,'H','R',"A"]]
    for i in range(1,26):
      assign(n)

    #insert code
  
  def assign(self,i):
    counter = 0
    
    for i in range(0,7)counter != 1:
      x = random.randint(2,14)
      counter = 0;            # Used to check if all the elements in n[i] have been occupied, iterates i to 4
      
      while(counter != 0):{
        if n[x][0] == 0:
          x = random.randint(2,14)
        
        else:
          append_tableau(x) 
            
      self.tableau[i][j] = 
    #insert code

# Used to add a card to the tabeau's seven card layer
# Checks whether each stack has the correct number of cards and then adds to the tableau
#
  def append_tableau(value):
    
    for i in range(0,7):
      x = len(self.tableau[i])
    
      if x <= (i+1):
        self.tabeau[i][x].append(value)
    
      else:
        

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