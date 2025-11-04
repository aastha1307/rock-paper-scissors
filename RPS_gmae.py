# RPS_game.py
import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    p1_wins = p2_wins = ties = 0

    for i in range(num_games):
        p1_move = player1(p2_prev_play)
        p2_move = player2(p1_prev_play)

        if verbose:
            print(f"Game {i+1}: Player1: {p1_move} | Player2: {p2_move}")

        if p1_move == p2_move:
            ties += 1
        elif (p1_move == 'R' and p2_move == 'S') or (p1_move == 'P' and p2_move == 'R') or (p1_move == 'S' and p2_move == 'P'):
            p1_wins += 1
        else:
            p2_wins += 1

        p1_prev_play = p1_move
        p2_prev_play = p2_move

    print(f"\nResults over {num_games} games:")
    print(f"Player1 wins: {p1_wins}")
    print(f"Player2 wins: {p2_wins}")
    print(f"Ties: {ties}\n")

    return {"p1_wins": p1_wins, "p2_wins": p2_wins, "ties": ties}


# --- Opponent Bots ---

def quincy(prev_play, opponent_history=[]):
    options = ["R", "P", "S", "R", "P"]
    if prev_play == "":
        opponent_history.clear()
    opponent_history.append(prev_play)
    return options[len(opponent_history) % len(options)]

def rando(prev_play):
    return random.choice(["R", "P", "S"])

def reflect(prev_play, opponent_history=[]):
    if prev_play == "":
        opponent_history.clear()
        return "R"
    opponent_history.append(prev_play)
    return prev_play

def cycle(prev_play, opponent_history=[]):
    options = ["R", "P", "S"]
    if prev_play == "":
        opponent_history.clear()
        return "R"
    last_move = opponent_history[-1] if opponent_history else "R"
    next_move = options[(options.index(last_move) + 1) % 3]
    opponent_history.append(next_move)
    return next_move
