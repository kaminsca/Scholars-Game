from hand import *
from hand_functions import function_dict
import random

LOW_RES = False
if LOW_RES: 
    from hand_images.hand_ascii_lowres import *
else:
    from hand_images.hand_ascii_v2 import *

class Player:
    def __init__(self, color):
        self.left = Hand(self)
        self.right = Hand(self)
        self.alive = True
        self.cpu = False
        self.color = color

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

    def print_hands(self):
        if not self.left.alive:
            print(self.color + hands_map[f"R{self.right.number}{self.right.state}"])
            print(bcolors.ENDC)
        elif not self.right.alive:
            print(self.color + combine_hands(empty, hands_map[f"L{self.left.number}{self.left.state}"]))
            print(bcolors.ENDC)
        else:
            print(self.color + combine_hands(hands_map[f"L{self.left.number}{self.left.state}"], hands_map[f"R{self.right.number}{self.right.state}"]) + bcolors.ENDC)

    def print_hands_upside_down(self):
        if not self.left.alive:
            print(self.color + flip_upside_down(hands_map[f"R{self.right.number}{self.right.state}"] + bcolors.ENDC))
        elif not self.right.alive:
            print(self.color +  combine_and_flip(empty, hands_map[f"L{self.left.number}{self.left.state}"] + bcolors.ENDC))
        else:
            print(self.color + combine_and_flip(hands_map[f"L{self.left.number}{self.left.state}"], hands_map[f"R{self.right.number}{self.right.state}"]) + bcolors.ENDC)
        print("\n"*3)

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
    
    def choose_new_state(self, hand):
        #TODO: print state with new (unchosen) hand sprite
        if hand.number == 4:
            # could get the wrong hand if both are 4, good enough for now
            return int(input(f'{"Left" if self.left == 4 else "Right"} hand changed to 4.\nChoose paper [0] or scissors [1]. This will not consume a turn.'))
        else:
            return int(input(f'{"Left" if self.left == 5 else "Right"} hand changed to 5.\nChoose paper [0] or rock [1]. This will not consume a turn.'))

class CPU(Player):
    def __init__(self):
        super().__init__(bcolors.FAIL)
        self.cpu = True
    
    def choose_action(self, cur, opp):
        if not cur.left.alive:
            hand = cur.right
        elif not cur.right.alive:
            hand = cur.left
        else:
            # cpu chooses action at random - left, right, or redistribution
            # disable redistribution if sum is either 9 or 10
            if cur.left.number + cur.right.number > 8:
                index = random.randint(0,1)
            else:
                index = random.randint(0,2)
            # redistribute
            if index == 2:
                new_vals = self.redistribution()
                print(f"Redistributing to {new_vals[0]}, {new_vals[1]}")
                return function_dict['Redistribute'][0], new_vals, [cur.left, cur.right]
            else:
                hand = cur.right if index else cur.left
        
        # pick random action from hand possibilities
        action_name = hand.actions[random.randint(0, len(hand.actions) - 1)]
        action = function_dict[action_name]
        func = action[0]
        # pick target of action
        num_targets = action[1]
        if num_targets == 0:
            target = None
        if num_targets == 1:
            # skip prompt if one hand dead 
            if not opp.left.alive:
                target = opp.right
            elif not opp.right.alive:
                target = opp.left
            else:
                target = opp.right if random.randint(0,1) else opp.left
        elif num_targets == 2:
            #TODO: let the CPU pick their own hands, check alive status of hands
            target = [opp.left, opp.right]
        
        print(action_name)
        return func, hand, target
    
    def redistribution(self):
        sum = self.left.number + self.right.number
        # pick random number between 0 and sum of hands, keep trying until passes validation
        while(1):
            new_left = random.randint(0, sum) # inclusive
            new_right = sum - new_left
            if new_left < 0 or new_right < 0 or new_left > 5 or new_right > 5:
                continue
            elif sum != new_left + new_right:
                continue
            elif new_left == self.left.number or new_left == self.right.number:
                continue
            return [new_left, new_right]

    def choose_new_state(self, hand):
        return random.randint(0,1)
