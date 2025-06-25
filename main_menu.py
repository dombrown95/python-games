import tkinter as tk

# Import game launcher functions
from magic_eight_ball_gui import run_magic_8_ball
from rock_paper_scissors_gui import run_rps
from tic_tac_toe_gui import run_tic_tac_toe
from chess_gui import run_chess
from connect_four_gui import run_connect_four

# Create main window
root = tk.Tk()
root.title("Game Menu")
root.geometry("320x400")
root.resizable(False, False)

# Title
tk.Label(root, text="Choose a Game", font=("Helvetica", 16)).pack(pady=20)

# Define games and launcher functions
games = [
    ("Magic 8 Ball", run_magic_8_ball),
    ("Rock Paper Scissors", run_rps),
    ("Tic Tac Toe", run_tic_tac_toe),
    ("Chess", run_chess),
    ("Connect Four", run_connect_four)
]

# Create a button for each game
for name, func in games:
    tk.Button(root, text=name, width=25, height=2, font=("Arial", 12),
              command=func).pack(pady=8)

# Run the main loop
root.mainloop()