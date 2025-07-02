import tkinter as tk
import random
from tkinter import messagebox

def run_tic_tac_toe():
    game_window = tk.Toplevel()
    game_window.title("Tic Tac Toe")
    game_window.lift()
    game_window.focus_force()
    game_window.grab_set()

    is_vs_computer = messagebox.askyesno("Game Mode", "Play against the computer?", parent=game_window)

    board = [""] * 9
    turn = ["X"]
    game_over = [False]
    result_text = tk.StringVar()

    def check_winner():
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in wins:
            if board[a] == board[b] == board[c] != "":
                return board[a]
        if "" not in board:
            return "Draw"
        return None

    def computer_move():
        empty = [i for i, val in enumerate(board) if val == ""]
        if empty:
            move = random.choice(empty)
            make_move(move)

    def make_move(i):
        if board[i] == "" and not game_over[0]:
            board[i] = turn[0]
            buttons[i].config(text=turn[0], state="disabled")
            winner = check_winner()
            if winner:
                game_over[0] = True
                if winner == "Draw":
                    result_text.set("It's a draw!")
                else:
                    result_text.set(f"{winner} wins!")
                restart_button.grid()  # Show restart button
                return
            turn[0] = "O" if turn[0] == "X" else "X"
            if is_vs_computer and turn[0] == "O":
                game_window.after(500, computer_move)

    def restart_game():
        for i in range(9):
            board[i] = ""
            buttons[i].config(text="", state="normal")
        turn[0] = "X"
        game_over[0] = False
        result_text.set("")
        restart_button.grid_remove()
        if is_vs_computer and turn[0] == "O":
            game_window.after(500, computer_move)

    buttons = []
    for i in range(9):
        b = tk.Button(
            game_window, text="", width=5, height=2, font=("Arial", 24),
            command=lambda i=i: make_move(i)
        )
        b.grid(row=i // 3, column=i % 3)
        buttons.append(b)

    tk.Label(game_window, textvariable=result_text, font=("Arial", 14)).grid(row=3, column=0, columnspan=3, pady=10)

    restart_button = tk.Button(game_window, text="Play Again", font=("Arial", 12), command=restart_game)
    restart_button.grid(row=4, column=0, columnspan=3, pady=5)
    restart_button.grid_remove()  # Hide initially

    if is_vs_computer and turn[0] == "O":
        game_window.after(500, computer_move)

if __name__ == "__main__":
    run_tic_tac_toe()