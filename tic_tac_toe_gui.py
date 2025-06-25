import tkinter as tk
from tkinter import messagebox

def run_tic_tac_toe():
    window = tk.Toplevel()
    window.title("Tic Tac Toe")

    board = [""] * 9
    turn = ["X"]

    def check_winner():
        wins = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
        for a, b, c in wins:
            if board[a] == board[b] == board[c] != "":
                return board[a]
        if "" not in board:
            return "Draw"
        return None

    def make_move(i):
        if board[i] == "":
            board[i] = turn[0]
            buttons[i].config(text=turn[0], state="disabled")
            winner = check_winner()
            if winner:
                if winner == "Draw":
                    messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                else:
                    messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
                window.destroy()
            turn[0] = "O" if turn[0] == "X" else "X"

    buttons = []
    for i in range(9):
        b = tk.Button(window, text="", width=5, height=2, font=("Arial", 24),
                      command=lambda i=i: make_move(i))
        b.grid(row=i//3, column=i%3)
        buttons.append(b)

if __name__ == "__main__":
    run_tic_tac_toe()