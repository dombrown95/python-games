import tkinter as tk
import random

def run_rps():
    wins = losses = ties = 0

    window = tk.Toplevel()
    window.title("Rock Paper Scissors")

    output = tk.StringVar()
    stats = tk.StringVar(value="Wins: 0  Losses: 0  Ties: 0")

    def play(player):
        nonlocal wins, losses, ties
        comp = random.choice(['Rock', 'Paper', 'Scissors'])

        if player == comp:
            ties += 1
            result = "It's a tie!"
        elif (player == 'Rock' and comp == 'Scissors') or \
             (player == 'Paper' and comp == 'Rock') or \
             (player == 'Scissors' and comp == 'Paper'):
            wins += 1
            result = "You win!"
        else:
            losses += 1
            result = "You lose!"

        stats.set(f"Wins: {wins}  Losses: {losses}  Ties: {ties}")
        output.set(f"You chose {player}, Computer chose {comp}. {result}")

    tk.Label(window, textvariable=output, font=("Arial", 12), wraplength=300).pack(pady=10)
    tk.Label(window, textvariable=stats).pack(pady=5)

    for move in ["Rock", "Paper", "Scissors"]:
        tk.Button(window, text=move, width=15, command=lambda m=move: play(m)).pack(pady=3)

if __name__ == "__main__":
    run_rps()