import random


def monty_hall_simulate(change_decision):
    boxes = [0, 1, 2]

    prize_box = random.choice(boxes)

    contestant_choice = random.choice(boxes)

    host_choices = [box for box in boxes if box != contestant_choice and box != prize_box]
    host_opens = random.choice(host_choices)

    if change_decision:
        remaining_boxes = [box for box in boxes if box != contestant_choice and box != host_opens]
        contestant_choice = remaining_boxes[0]

    win = contestant_choice == prize_box

    return win

simulations = 10000
change_wins = 0
stay_wins = 0

for _ in range(simulations):
    if monty_hall_simulate(change_decision=True):
        change_wins += 1
    if monty_hall_simulate(change_decision=False):
        stay_wins += 1

print(f"Zmiana wyboru: Wygrane = {change_wins}/{simulations} ({(change_wins / simulations) * 100}%)")
print(f"Bez zmiany wyboru: Wygrane = {stay_wins}/{simulations} ({(stay_wins / simulations) * 100}%)")