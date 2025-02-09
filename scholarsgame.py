from player import *
from hand_functions import function_dict

def get_turn_inputs(cur, opp):
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
            new_vals = redistribution()
            return function_dict['Redistribute'][0], new_vals, [cur.left, cur.right]
        else:
            hand = cur.right if index else cur.left
    hand.print_actions()
    # get action
    action_ind = int(input("Choose an action: "))
    action_key = hand.actions[action_ind]
    action = function_dict[action_key]
    action_function = action[0]
    
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
    return action_function, hand, target

def redistribution():
    user_input = input("Input two numbers to redistribute your hands' values: ")
    vals = []
    for letter in user_input:
        if letter.isdigit():
            vals.append(letter)
    new_left = int(vals[0])
    new_right = int(vals[1])

    return [new_left, new_right]

def end_game_check(player1, player2, turns):
    if not player1.left.alive and not player1.right.alive:
        print("\n--- Game Over ---")
        print(f"Congrats Player 2 for winning after {turns} turns!")
        return True
    if not player2.left.alive and not player2.right.alive:
        print("\n--- Game Over ---")
        print(f"Congrats Player 1 for winning after {turns} turns!")
        return True
    return False

def play_game(player1, player2):
    turn = 0
    while player1.alive and player2.alive:
        if turn % 2 == 0:
            cur = player1
            opp = player2
        else:
            cur = player2
            opp = player1
        print(f"\n--- {turn % 2 + 1}'s turn ---")
        cur.print_player()
        print('Opponent: ', end="")
        opp.print_player()
        
        func, hand, target = get_turn_inputs(cur, opp)
        try:
            func(hand, target)
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            continue
            
        # check status:
        if end_game_check(player1, player2, turn):
            return
        
        # update
        if isinstance(target, list):
            for targ in target:
                targ.set_actions()
        elif target != None:
            target.set_actions()
        turn += 1

if __name__ == '__main__':
    play_game(Player(), Player())