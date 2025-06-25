import tkinter as tk
import chess
from tkinter import messagebox
import random

SQUARE_SIZE = 60
BOARD_SIZE = SQUARE_SIZE * 8

UNICODE_PIECES = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}

class ChessGUI:
    def __init__(self, root, vs_computer=False):
        self.root = root
        self.root.title("Chess")
        self.board = chess.Board()
        self.selected_square = None
        self.vs_computer = vs_computer

        # UI components
        self.turn_label = tk.Label(root, text="White's turn", font=("Arial", 12))
        self.turn_label.pack(pady=5)

        self.canvas = tk.Canvas(root, width=BOARD_SIZE, height=BOARD_SIZE)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.draw_board()

        if self.vs_computer and not self.board.turn:
            self.root.after(500, self.computer_move)

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row)
                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE

                color = "#EEE" if (row + col) % 2 == 0 else "#999"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                # Highlight selected square
                if self.selected_square == square:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="yellow", width=4)

                piece = self.board.piece_at(square)
                if piece:
                    symbol = UNICODE_PIECES[piece.symbol()]
                    self.canvas.create_text(
                        x1 + SQUARE_SIZE / 2,
                        y1 + SQUARE_SIZE / 2,
                        text=symbol,
                        font=("Arial", 28)
                    )

        self.turn_label.config(text="White's turn" if self.board.turn else "Black's turn")

    def on_click(self, event):
        if self.board.is_game_over() or (self.vs_computer and not self.board.turn):
            return

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
                    self.end_game()
                    return
                if self.vs_computer:
                    self.root.after(500, self.computer_move)
            else:
                self.selected_square = None

        self.draw_board()

    def computer_move(self):
        if not self.board.is_game_over():
            move = random.choice(list(self.board.legal_moves))
            self.board.push(move)
            self.draw_board()
            if self.board.is_game_over():
                self.end_game()

    def end_game(self):
        result = self.board.result()
        messagebox.showinfo("Game Over", f"Result: {result}")
        self.root.destroy()

def run_chess():
    game_window = tk.Toplevel()
    game_window.title("Chess")
    vs_computer = messagebox.askyesno("Game Mode", "Play against the computer?", parent=game_window)
    
    ChessGUI(game_window, vs_computer)

    # Bring game window to front
    game_window.lift()
    game_window.focus_force()
    game_window.grab_set()

if __name__ == "__main__":
    run_chess()