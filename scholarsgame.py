from player import *
from hand_functions import function_dict

def get_turn_inputs(cur, opp):
    # get hand to use
    #TODO: skip prompt if one hand dead
    hand_ind = int(input(f"Use left ({cur.left.number}) or right ({cur.right.number}) hand with 0 or 1: "))
    hand = cur.right if hand_ind else cur.left
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
        opp_hand_ind = int(input(f"On opponent's left ({opp.left.number}) or right ({opp.right.number}) hand with 0 or 1: "))
        target = opp.right if opp_hand_ind else opp.left
    elif num_targets == 2:
        #TODO: let the user pick their own hands
        target = [opp.left, opp.right]
    return action_function, hand, target

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
        else:
            target.set_actions()

        turn += 1


if __name__ == '__main__':
    play_game(Player(), Player())