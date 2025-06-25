import tkinter as tk
import chess
from tkinter import messagebox

SQUARE_SIZE = 60
BOARD_SIZE = SQUARE_SIZE * 8

# Unicode piece symbols
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

        self.canvas = tk.Canvas(root, width=BOARD_SIZE, height=BOARD_SIZE)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE

                color = "#EEE" if (row + col) % 2 == 0 else "#999"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

                square = chess.square(col, 7 - row)
                piece = self.board.piece_at(square)
                if piece:
                    symbol = UNICODE_PIECES[piece.symbol()]
                    self.canvas.create_text(
                        x1 + SQUARE_SIZE / 2,
                        y1 + SQUARE_SIZE / 2,
                        text=symbol,
                        font=("Arial", 28)
                    )

    def on_click(self, event):
        col = event.x // SQUARE_SIZE
        row = event.y // SQUARE_SIZE
        square = chess.square(col, 7 - row)

        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.draw_board()
                if self.board.is_game_over():
                    messagebox.showinfo("Game Over", f"Result: {self.board.result()}")
                    self.root.destroy()
            else:
                self.selected_square = None  # Reset on invalid move

def run_chess():
    chess_window = tk.Toplevel()
    ChessGUI(chess_window)

if __name__ == "__main__":
    run_chess()