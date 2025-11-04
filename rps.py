# RPS.py
import random

def _beat(move):
    return {'R': 'P', 'P': 'S', 'S': 'R'}[move]

def _most_common(seq):
    if not seq:
        return None
    return max(('R', 'P', 'S'), key=lambda m: seq.count(m))

def _predict_cycle(seq, max_cycle=6):
    n = len(seq)
    if n < 4:
        return None
    for cycle_len in range(1, min(max_cycle, n//2)+1):
        pattern = seq[-cycle_len:]
        ok = True
        repeats = n // cycle_len
        if repeats < 2:
            continue
        for i in range(1, min(repeats, 4)):
            if seq[-cycle_len*(i+1):-cycle_len*i] != pattern:
                ok = False
                break
        if ok:
            return pattern[0]
    return None

def player(prev_play, opponent_history=[], my_history=[]):
    if prev_play == '':
        opponent_history.clear()
        my_history.clear()
        opening = random.choice(['R','P','S'])
        my_history.append(opening)
        return opening

    opponent_history.append(prev_play)

    # detect opponent bias
    if len(opponent_history) >= 6:
        recent = opponent_history[-12:]
        most = _most_common(recent)
        freq = recent.count(most) / len(recent)
        if freq >= 0.6:
            move = _beat(most)
            my_history.append(move)
            return move

    # detect copycat
    if len(my_history) >= 2 and len(opponent_history) >= 2:
        pairs_checked = min(len(my_history)-1, len(opponent_history)-1, 12)
        copy_count = 0
        for i in range(1, pairs_checked+1):
            if opponent_history[-i] == my_history[-i-1]:
                copy_count += 1
        if pairs_checked > 0 and (copy_count / pairs_checked) >= 0.6:
            move = _beat(my_history[-1])
            my_history.append(move)
            return move

    # detect cycles
    predicted = _predict_cycle(opponent_history, max_cycle=6)
    if predicted:
        move = _beat(predicted)
        my_history.append(move)
        return move

    # fallback frequency counter
    common = _most_common(opponent_history[-20:])
    if common:
        move = _beat(common)
        if random.random() < 0.10:
            move = random.choice(['R','P','S'])
        my_history.append(move)
        return move

    move = random.choice(['R','P','S'])
    my_history.append(move)
    return move
