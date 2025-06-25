import tkinter as tk
from magic_eight_ball_gui import run_magic_8_ball
from rock_paper_scissors_gui import run_rps
from tic_tac_toe_gui import run_tic_tac_toe
from chess_gui import run_chess

root = tk.Tk()
root.title("Game Menu")
root.geometry("300x350")

tk.Label(root, text="Choose a Game", font=("Helvetica", 16)).pack(pady=20)

games = [
    ("Magic 8 Ball", run_magic_8_ball),
    ("Rock Paper Scissors", run_rps),
    ("Tic Tac Toe", run_tic_tac_toe),
    ("Chess", run_chess),
]

for name, func in games:
    tk.Button(root, text=name, width=25, height=2, command=func).pack(pady=8)

root.mainloop()