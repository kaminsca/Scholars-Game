from hand_functions import *

class Hand:
    # state has meaning for a number of 4 or 5:
    # state 0 for hand 4 is paper, 1 is scissors
    # state 0 for hand 5 is paper, 1 is rock
    def __init__(self, number, state):
        self.number = number
        self.state = state
        self.actions = []
        self.alive = True
        self.set_actions()
        
    def set_actions(self):
        #TODO: only show valid moves given current state
        number = self.number
        state = self.state
        self.actions = ['Add']
        # self.actions.append('Redistribute')
        if number == 1:
            self.actions.append('Plumb')
        elif number == 2:
            self.actions.append('Cut')
            self.actions.append('Double Plumb')
        elif number == 3:
            self.actions.append('Double Cut')
            self.actions.append('Double Plumb')
        elif number == 4:
            if state == 0:
                self.actions.append('Paper')
            else:
                self.actions.append('Cut')
            self.actions.append('Swap State')
        elif number == 5:
            if state == 0:
                self.actions.append('Paper')
            else:
                self.actions.append('Rock')
            self.actions.append('Swap State')

    def kill_hand(self):
        self.alive = False

    def print_actions(self):
        for index, action in enumerate(self.actions):
            print(f'   {index}: {action}')
            
    def print_hand(self):
        print(f'Hand: {self.number}')
        print(f'Alive: {self.alive}')
        print('Actions: ')
        self.print_actions()

if __name__ == '__main__':
    hand1 = Hand(1,0)
    hand1.print_hand()