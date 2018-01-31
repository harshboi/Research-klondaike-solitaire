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
    self.tableau = []
  
  def shuffle(self):
    #11 = K, 12 = Q, 13 = J, 14 = A
    n[0] = n[1] = []    
    for i in range(2,10):
      n[i] = [[1,'C','B'],[1,'D','R'],[1,'H','R'],[1,'S','B']]
    #n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n10 = [[1,'C','B'],[1,'D','R'],[1,'H','R'],[1,'S','B']]    #[[1,'c',b']] where 1 = no. of cards in the deck, c = club, b = black
    n[11] = [[1,'C','B'],[1,'S','B'],[1,'D','R'],[1,'H','R']]
    n[12] = [[1,'C','B'],[1,'S','B'],[1,'D','R'],[1,'H','R']]
    n[13] = [[1,'C','B'],[1,'S','B'],[1,'D','R'],[1,'H','R']]
    n[14] = [[1,'C','B'],[1,'S','B'],[1,'D','R'],[1,'H','R']]     
    for i in range(1,26):
      assign(i)

    #insert code
  
  def assign(self,i):
    counter = 0
    while counter != 1:
      random.randint(2,14)
      n[i] = self.tableau()
    #insert code


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