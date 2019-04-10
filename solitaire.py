import copy
import numpy as np
import os
import pygame
import sys
sys.path.append('../')
from abstract import abstract_state
from dealers.simulators.solitairecode import solitaire
import pdb


class SolitaireState(abstract_state.AbstractState):
    env_name = "Solitaire"
    num_players = 1

    def __init__(self):
        pdb.set_trace()
        self.current_state = solitaire.game()
        self.current_state.shuffle()
        self.game_outcome = None  # 0 - player 1 won, 'draw' - draw, 1 - player 2 won, None - game not over
        self.helperr = []
        self.resources = {}  # sprites for pygame
        self.f = open("../../../actions.txt", "a")
        self.tableau = open("../../../tableau.txt", "a")
        self.past_state = []  # will only store the tableau and foundation and will be checked to prevent redundant actions from taking place


    def reinitialize(self):  # called after one entire game has been played
        self.current_state = solitaire.game()
        self.current_state.shuffle()  # set up initial piece configuration
        self.current_player = 0
        self.game_outcome = None
        pdb.set_trace()

    def clone(self):            # Internal Python3.6 function
        new_state = copy.copy(self)
        new_state.current_state = copy.copy(self.current_state)
        return new_state

    def set(self, state):
        self.current_state = state.current_state        # ADD
        # self.current_player = state.current_player
        self.game_outcome = state.game_outcome

    def take_action(self, action):
        # reward = self.current_state.move_piece(action)

        reward = self.current_state.take_action(action)
        # for i in range (len(self.past_state)):
            # if (self.past_state[i][0] == self.current_state.talon and self.past_state[i][1] == self.current_state.tableau and self.past_state[i][2] == self.current_state.foundation):
                # reward = -10
        # if (self.current_state.last_action != None):
            # self.current_state.second_last_action = self.current_state.last_action
        # if (self.current_state.second_last_action == action):
            # reward = -10
        # IMPLEMENT a call that actually moves stuff
        self.current_state.last_action = action   # Setup functions for last_action  ERROR  // Global CHANGE of previous_player to previous_action
        # self.current_state.last_action, previous_state = action, self.current_player   # Setup functions for last_action  ERROR  // Global CHANGE of previous_player to previous_action
        # self.update_current_player()                # Can be found in abstract_state.py  # not needed as solitaire is a single player game

        self.current_state.cached_actions = []
        self.get_actions()  # Line 53
        # fetch_reward = self.current_state.get_reward(action)
        # if (self.current_state.return_game_state == 1):
            # pdb.set_trace
        if (len(self.current_state.cached_actions) == 0):
            # pdb.set_trace()
            self.game_outcome = 'win' if self.current_state.return_game_state else None
            # if self.game_outcome == 'win':
            # print("Game over")
        # pdb.set_trace()
        # self.helperr.append(action)
        # self.f.write(action)
        # self.f.write("\n")
        # self.tableau.write(str(self.current_state.tableau))
        # self.tableau.write("\n")
        # print reward
        # print (reward)
        # if(type(reward) != )
        # self.past_state.append([self.current_state.talon,self.current_state.tableau,self.current_state.foundation])
        self.helperr.append(self.current_state.foundation)
        if(str(type(reward)) != "<class 'int'>"):
            print (str(type(reward)))
            pdb.set_trace()
        return np.array([reward])
        # if self.current_state.return_game_state == 1:
            # self.game_outcome = previous_player if self.current_state.is_checked(self.get_current_color()) else 'draw'

        # The current player gets the opposite of the reward (e.g. losing a piece)
        # return np.array([-1 * reward if player_idx == self.current_player else reward
                        #  for player_idx in range(self.num_players)])

    def get_actions(self):
        if len(self.current_state.cached_actions) == 0:
            self.current_state.cached_actions = self.current_state.get_actions()
        # if len(self.current_state.cached_actions) == 0:
            # pdb.set_trace()
        return self.current_state.cached_actions

    # def get_current_color(self):
        # return 'white' if self.current_player == 0 else 'black'

    def get_value_bounds(self):
        # pdb.set_trace()
        king_value = self.current_state.piece_values['k']  # defeat / victory
        queen_value = self.current_state.piece_values['q']
        return {'defeat': -1 * king_value, 'victory': king_value,
                'min non-terminal': -1 * queen_value, 'max non-terminal': queen_value,
                'pre-computed min': None, 'pre-computed max': None,
                'evaluation function': None}

    def is_terminal(self):
        return self.game_outcome is not None


    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return self.current_state.__str__()  # print board
