import tkinter as tk
import subprocess
import sys
import os

def launch_game(script_name):
    """Launch a game script in a new process."""
    if getattr(sys, 'frozen', False):  # If bundled with PyInstaller
        script_path = os.path.join(sys._MEIPASS, script_name)
    else:
        script_path = os.path.abspath(script_name)

    subprocess.Popen([sys.executable, script_path])

# Create main window
root = tk.Tk()
root.title("Game Menu")
root.geometry("300x300")
root.resizable(False, False)

# Title Label
label = tk.Label(root, text="Select a Game", font=("Helvetica", 16))
label.pack(pady=20)

# Buttons for each game
games = {
    "Chess": "chess.py",
    "Rock Paper Scissors": "rock_paper_scissors.py",
    "Magic 8 Ball": "magic_eight_ball.py",
    "Tic Tac Toe": "tic_tac_toe.py"
}

for game_name, script in games.items():
    button = tk.Button(root, text=game_name, width=25, height=2, command=lambda s=script: launch_game(s))
    button.pack(pady=5)

# Run the main loop
root.mainloop()