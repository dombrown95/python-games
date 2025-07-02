import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import messagebox

def run_rps():
    window = tk.Toplevel()
    window.title("Rock Paper Scissors")
    window.lift()
    window.focus_force()
    window.grab_set()

    vs_computer = messagebox.askyesno("Game Mode", "Play against the computer?", parent=window)

    wins = losses = ties = 0
    choices = ['rock', 'paper', 'scissors']
    player1_choice = None

    # Load and resize images
    images = {
        c: ImageTk.PhotoImage(Image.open(f"{c}.png").resize((100, 100)))
        for c in choices
    }

    canvas = tk.Canvas(window, width=300, height=140)
    canvas.grid(row=0, column=0, columnspan=3, pady=10)

    user_sprite = canvas.create_image(50, 80, image=images['rock'])
    comp_sprite = canvas.create_image(250, 80, image=images['rock'])

    canvas.create_text(50, 25, text="You", font=("Arial", 10))
    canvas.create_text(250, 25, text=("Computer" if vs_computer else "Player 2"), font=("Arial", 10))

    output = tk.StringVar()
    stats = tk.StringVar(value="Wins: 0  Losses: 0  Ties: 0")
    prompt = tk.StringVar(value="Player 1, choose:")

    tk.Label(window, textvariable=output, font=("Arial", 12)).grid(row=1, column=0, columnspan=3, pady=5)
    tk.Label(window, textvariable=stats).grid(row=2, column=0, columnspan=3)
    tk.Label(window, textvariable=prompt, font=("Arial", 10)).grid(row=3, column=0, columnspan=3, pady=(10, 0))

    btn_frame = tk.Frame(window)
    btn_frame.grid(row=4, column=0, columnspan=3, pady=10)

    def handle_choice(choice):
        nonlocal wins, losses, ties, player1_choice

        if not vs_computer:
            if player1_choice is None:
                player1_choice = choice
                canvas.itemconfig(user_sprite, image=images[choice])
                prompt.set("Player 2, choose:")
                return
            else:
                player2_choice = choice
                canvas.itemconfig(comp_sprite, image=images[player2_choice])

                # Determine winner
                if player1_choice == player2_choice:
                    ties += 1
                    result = "It's a tie!"
                elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
                     (player1_choice == 'paper' and player2_choice == 'rock') or \
                     (player1_choice == 'scissors' and player2_choice == 'paper'):
                    wins += 1
                    result = "Player 1 wins!"
                else:
                    losses += 1
                    result = "Player 2 wins!"

                stats.set(f"Wins: {wins}  Losses: {losses}  Ties: {ties}")
                output.set(f"Player 1 chose {player1_choice} and Player 2 chose {player2_choice}. \n{result}")
                player1_choice = None
                prompt.set("Player 1, choose:")

        else:
            comp_choice = random.choice(choices)
            canvas.itemconfig(user_sprite, image=images[choice])
            canvas.itemconfig(comp_sprite, image=images[comp_choice])

            if choice == comp_choice:
                ties += 1
                result = "It's a tie!"
            elif (choice == 'rock' and comp_choice == 'scissors') or \
                 (choice == 'paper' and comp_choice == 'rock') or \
                 (choice == 'scissors' and comp_choice == 'paper'):
                wins += 1
                result = "You win!"
            else:
                losses += 1
                result = "You lose!"

            stats.set(f"Wins: {wins}  Losses: {losses}  Ties: {ties}")
            output.set(f"You chose {choice}, opponent chose {comp_choice}. {result}")

    for c in choices:
        tk.Button(btn_frame, text=c.capitalize(), width=12, command=lambda ch=c: handle_choice(ch)).pack(side="left", padx=8)

if __name__ == "__main__":
    run_rps()