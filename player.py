from hand import *
from hand_functions import function_dict

class Player:
    def __init__(self):
        self.left = Hand(1,0)
        self.right = Hand(1,0)
        self.alive = True
        self.cpu = False

    def print_choices(self):
        choices = set()
        for index, action in enumerate(self.left.actions):
            choices.add(action)
        for index, action in enumerate(self.right.actions):
            choices.add(action)
        for index, choice in enumerate(choices):
            print(f'{index}: {choice}')

    def print_player(self):
        if self.left.alive:
            print(f'Left: {self.left.number}', end=", ")
            if self.left.number == 4:
                if self.left.state == 0:
                    print('(paper)', end=", ")
                else:
                    print('(scissors)', end=", ")
            elif self.left.number == 5:
                if self.left.state == 0:
                    print('(paper)', end=", ")
                else:
                    print('(rock)', end=", ")
        if self.right.alive:
            print(f'Right: {self.right.number}', end="")  
            if self.right.number == 4:
                if self.right.state == 0:
                    print(' (paper)', end="") 
                else:
                    print(' (scissors)', end="")
            elif self.right.number == 5:
                if self.right.state == 0:
                    print(' (paper)', end="")
                else:
                    print(' (rock)', end="")
        print('\n')

    def choose_action(self, cur, opp):
        # get hand to use
        # skip prompt if one hand dead 
        if not cur.left.alive:
            hand = cur.right
            print(f"Using right ({cur.right.number}).")
        elif not cur.right.alive:
            hand = cur.left
            print(f"Using left ({cur.left.number}).")
        else:
            index = int(input(f"Use left ({cur.left.number}) hand with [0], right ({cur.right.number}) hand with [1], or redistribute your hands with [2]: "))
            if index == 2:
                # redistribute
                new_vals = self.redistribution()
                return function_dict['Redistribute'][0], new_vals, [cur.left, cur.right]
            else:
                hand = cur.right if index else cur.left
        hand.print_actions()
        # get action
        action_ind = int(input("Choose an action: "))
        action_key = hand.actions[action_ind]
        action = function_dict[action_key]
        func = action[0]
        
        # determine the number of targets
        num_targets = action[1]
        if num_targets == 0:
            target = None
        if num_targets == 1:
            # skip prompt if one hand dead 
            if not opp.left.alive:
                target = opp.right
                print(f"On opponent's right ({opp.right.number}).")
            elif not opp.right.alive:
                target = opp.left
                print(f"On opponent's left ({opp.left.number}).")
            else:
                opp_hand_ind = int(input(f"On opponent's left ({opp.left.number}) or right ({opp.right.number}) hand with 0 or 1: "))
                target = opp.right if opp_hand_ind else opp.left
        elif num_targets == 2:
            #TODO: let the user pick their own hands, check alive status of hands
            target = [opp.left, opp.right]
        return func, hand, target
    
    def redistribution(self):
        user_input = input("Input two numbers to redistribute your hands' values: ")
        vals = []
        for letter in user_input:
            if letter.isdigit():
                vals.append(letter)
        new_left = int(vals[0])
        new_right = int(vals[1])

        return [new_left, new_right]

#TODO: finish creating CPU, move choosing actions from scholarsgame.py into here
class CPU(Player):
    def __init__(self):
        super().__init__()
        self.cpu = True
    
    def choose_action(self, cur, opp):
        return 1