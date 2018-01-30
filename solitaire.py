import random
import math

class game:
  def __init__(self):
    self.cards = {'K':[['B','S'],['B','C'],['R','D'],['R','D']],"Q":[['B','S'],['B','C'],['R','D'],['R','D']],"J":[['B','S'],['B','C'],['R','D'],['R','D']],"A":[['B','S'],['B','C'],['R','D'],['R','D']],"2":[['B','S'],['B','C'],['R','D'],['R','D']],"3":[['B','S'],['B','C'],['R','D'],['R','D']]}
    self.cards.update({"4":[['B','S'],['B','C'],['R','D'],['R','D']],"5":[['B','S'],['B','C'],['R','D'],['R','D']],"6":[['B','S'],['B','C'],['R','D'],['R','D']],"7":[['B','S'],['B','C'],['R','D'],['R','D']],"8":[['B','S'],['B','C'],['R','D'],['R','D']],"9":[['B','S'],['B','C'],['R','D'],['R','D']],"10":[['B','S'],['B','C'],['R','D'],['R','D']]})
    self.turnstock = {}
    self.foundation = {}
    self.talon = {}
  
  def shuffle(self):
      self.cards = {'K':[[B,S],[B,C],[R,D],[R,D]],"Q":[[B,S],[B,C],[R,D],[R,D]],"J":[[B,S],[B,C],[R,D],[R,D]],"A":[[B,S],[B,C],[R,D],[R,D]],"2":[[B,S],[B,C],[R,D],[R,D]],"3":[[B,S],[B,C],[R,D],[R,D]]}
      self.cards.update({"4":[[B,S],[B,C],[R,D],[R,D]],"5":[[B,S],[B,C],[R,D],[R,D]],"6":[[B,S],[B,C],[R,D],[R,D]],"7":[[B,S],[B,C],[R,D],[R,D]],"8":[[B,S],[B,C],[R,D],[R,D]],"9":[[B,S],[B,C],[R,D],[R,D]],"10":[[B,S],[B,C],[R,D],[R,D]]})
    #insert code
  
  #def display_talon(self):
    #insert code

  #def display_foundations(self):
    #insert code
  

  #def display_stock(self):
    #insert code


  #def display_tableau(self):
    #insert code


def main():
  a = game()
  print(a.cards.keys())

main()