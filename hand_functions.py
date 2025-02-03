# Functions
def add(hand, target_hand):
    target_hand.number = (target_hand.number + hand.number - 1) % 5 + 1
    return 1

def test():
    raise ValueError('hello')

def plumb(hand, target_hand):
    # 1 beats rock
    if target_hand.number != 5 or target_hand.state != 1:
        raise ValueError("invalid target")
    target_hand.kill_hand()
    return 1

def cut(hand, target_hand):
    # 2, 4 scissors beat paper, or turn 1 into rock
    if target_hand.number == 1:
        target_hand.number = 5
        target_hand.state = 1
        return 1
    if not (target_hand.number == 4 and target_hand.state == 0):
        raise ValueError("invalid target")
    target_hand.kill_hand()
    return

def double_plumb(hand, target_hands):
    # 2 or 3 scissors beats two rocks
    for targ in target_hands:
        if not (targ.number == 5 and targ.state == 1):
            raise ValueError("invalid target")
    for targ in target_hands:
        targ.kill_hand()
    return 1

def double_cut(hand, target_hands):
    # 3 cuts two papers, two ones, or a mix at once
    for targ in target_hands:
        if not (targ.number == 5 and targ.state == 1) or (targ.number == 4 and targ.state == 0):
            raise ValueError("invalid target")
    for targ in target_hands:
        if targ.number == 1:
            targ.number = 5
            targ.state = 1
            return 1
        else:
            targ.kill_hand()
    return

def paper(hand, target_hand):
    # 4 or 5 paper beats rock
    if not (target_hand.number == 5 and target_hand.state == 1):
        raise ValueError("invalid target")
    target_hand.kill_hand()
    return 1

def rock(hand, target_hand):
    # 5 rock beats any scissors
    if not target_hand.number == 2 or target_hand.number == 3 or (target_hand.number == 4 and target_hand.state == 1):
        raise ValueError("invalid target")
    target_hand.kill_hand()
    return

def swap_state(hand):
    # 4 swaps between paper and scissors
    # 5 swaps between rock and paper
    if hand.number == 4 or hand.number == 5:
        hand.state = 1 - hand.state
        return 1
    raise ValueError("invalid target")

# key: function name, value: (function, number of targets) 
function_dict = {
    'Add': (add, 1),
    'Test': (test, 0),
    'Plumb': (plumb, 1),
    'Cut': (cut, 1),
    'Double Plumb': (double_plumb, 2),
    'Double Cut': (double_cut, 2),
    'Paper': (paper, 1),
    'Rock': (rock, 1),
    'Swap State': (swap_state, 0)
}