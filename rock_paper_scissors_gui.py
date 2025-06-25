import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import simpledialog, messagebox

def run_rps():
    window = tk.Toplevel()
    window.title("Rock Paper Scissors")
    window.lift()
    window.focus_force()
    window.grab_set()

    vs_computer = messagebox.askyesno("Game Mode", "Play against the computer?", parent=window)

    wins = losses = ties = 0
    choices = ['rock', 'paper', 'scissors']

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

    tk.Label(window, textvariable=output, font=("Arial", 12)).grid(row=1, column=0, columnspan=3, pady=5)
    tk.Label(window, textvariable=stats).grid(row=2, column=0, columnspan=3)

    def play(player_choice):
        nonlocal wins, losses, ties

        if vs_computer:
            comp_choice = random.choice(choices)
        else:
            comp_choice = simpledialog.askstring("Player 2", "Enter move (rock, paper, or scissors):", parent=window)
            if comp_choice not in choices:
                messagebox.showerror("Invalid", "Move must be rock, paper, or scissors")
                return

        canvas.itemconfig(user_sprite, image=images[player_choice])
        canvas.itemconfig(comp_sprite, image=images[comp_choice])

        if player_choice == comp_choice:
            ties += 1
            result = "It's a tie!"
        elif (player_choice == 'rock' and comp_choice == 'scissors') or \
             (player_choice == 'paper' and comp_choice == 'rock') or \
             (player_choice == 'scissors' and comp_choice == 'paper'):
            wins += 1
            result = "You win!"
        else:
            losses += 1
            result = "You lose!" if vs_computer else "Player 2 wins!"

        stats.set(f"Wins: {wins}  Losses: {losses}  Ties: {ties}")
        output.set(f"You chose {player_choice}, opponent chose {comp_choice}. {result}")

    # Buttons to choose move
    btn_frame = tk.Frame(window)
    btn_frame.grid(row=3, column=0, columnspan=3, pady=10)

    for choice in choices:
        tk.Button(btn_frame, text=choice.capitalize(), width=12,
                  command=lambda c=choice: play(c)).pack(side="left", padx=8)

if __name__ == "__main__":
    run_rps()