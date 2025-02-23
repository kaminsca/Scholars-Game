from player import *
from hand_functions import function_dict

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

        # print game state to player
        if not cur.cpu:
            cur.print_player()
            print('Opponent: ', end="")
            opp.print_player()
            opp.print_hands_upside_down()
            cur.print_hands()
        
        # func, hand, target = get_turn_inputs(cur, opp)
        func, hand, target = cur.choose_action(cur, opp)
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
    # play_game(Player(color=bcolors.BOLD), Player(color=bcolors.OKGREEN))
    play_game(Player(bcolors.BOLD), CPU())
    # print(combine_hands(L2, R3))
    # print(empty)