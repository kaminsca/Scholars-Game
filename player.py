from hand import *

class Player:
    def __init__(self):
        self.left = Hand(1,0)
        self.right = Hand(1,0)
        self.alive = True

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