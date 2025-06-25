import tkinter as tk
from tkinter import messagebox
import importlib

# Mapping of game names to their importable module and callable function
games = {
    "Chess": ("chess_gui", "run_chess"),
    "Tic Tac Toe": ("tic_tac_toe_gui", "run_tic_tac_toe"),
    "Rock Paper Scissors": ("rock_paper_scissors_gui", "run_rps"),
    "Connect Four": ("connect_four_gui", "run_connect_four"),
    "Magic 8 Ball": ("magic_eight_ball_gui", "run_magic_eight_ball"),
}

def launch_game(game_name):
    module_name, function_name = games[game_name]
    try:
        game_module = importlib.import_module(module_name)
        game_func = getattr(game_module, function_name)
        game_func()
    except Exception as e:
        messagebox.showerror("Error", f"Could not launch {game_name}.\n\n{e}")

def main():
    root = tk.Tk()
    root.title("Game Menu")
    root.geometry("400x400")
    root.resizable(False, False)

    tk.Label(root, text="Select a Game", font=("Arial", 18)).pack(pady=20)

    for game in games:
        tk.Button(
            root,
            text=game,
            font=("Arial", 14),
            width=25,
            pady=5,
            command=lambda g=game: launch_game(g)
        ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()