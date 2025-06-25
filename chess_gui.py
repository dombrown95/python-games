import tkinter as tk
import chess
from tkinter import messagebox

UNICODE_PIECES = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess")
        self.board = chess.Board()
        self.selected_square = None
        self.buttons = {}
        self.build_board()

    def build_board(self):
        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row)
                b = tk.Button(self.root, width=4, height=2,
                              font=('Arial', 24),
                              command=lambda s=square: self.on_click(s))
                b.grid(row=row, column=col)
                self.buttons[square] = b
        self.update_board()

    def on_click(self, square):
        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.update_board()
                if self.board.is_game_over():
                    result = self.board.result()
                    messagebox.showinfo("Game Over", f"Result: {result}")
                    self.root.destroy()
            else:
                self.selected_square = None

    def update_board(self):
        for square, button in self.buttons.items():
            piece = self.board.piece_at(square)
            symbol = UNICODE_PIECES.get(piece.symbol()) if piece else " "
            button.config(text=symbol)

def run_chess():
    chess_window = tk.Toplevel()
    ChessGUI(chess_window)