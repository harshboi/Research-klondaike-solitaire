# import one

# print("top-level in two.py")
# one.func()

# if __name__ == "__main__":
#     print("two.py is being run directly")
# else:
#     print("two.py is being imported into another module")


def get_actions():
    possible_actions = []
    for i in range(7):
      # if(len(self.tableau[i]) > 0):
        string_builder = "fl"               #fl - flip the talon
        possible_actions.append(string_builder)
        for i in range(7):    # 7 is the number of tableaus
          string_builder = "t to ta" + str(i)   # t to ta1 - talon to tableau
          # legality = is_legal(string_builder)
          possible_actions.append(string_builder)
          for j in range(7):
            if (i!=j):
              string_builder = "ta" + str(i) + " to ta" + str(j)   # ta1 to ta2 - tabelau to tableau
              # legality = is_legal(string_builder);
              possible_actions.append(string_builder)
          for j in range(4):
            string_builder = "ta"+str(i)+"to f"+str(j)    # ta1 to f1 - tableau to foundation
            # legality = is_legal(string_builder)
            possible_actions.append(string_builder)
            string_builder = "t to f"+str(j)     # t to f1 - talon to foundation
            # legality = is_legal(string_builder)
            possible_actions.append(string_builder)
    for i in range(len(possible_actions)):
      print(possible_actions[i]+"\n")

    print(len(possible_actions))
    # return chain.from_iterable([func(self) for func in possible_actions])  #generate actions and flatten lists   # known as single line functions for lists REFERENCE

get_actions()