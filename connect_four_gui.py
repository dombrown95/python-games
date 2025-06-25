import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLUMNS = 7
CELL_SIZE = 70
PLAYER_COLORS = ["red", "yellow"]

def run_connect_four():
    class ConnectFour:
        def __init__(self, root):
            self.root = root
            self.root.title("Connect Four")
            self.current_player = 0  # 0 = Red, 1 = Yellow
            self.board = [["" for _ in range(COLUMNS)] for _ in range(ROWS)]

            self.canvas = tk.Canvas(root, width=COLUMNS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="blue")
            self.canvas.pack()
            self.canvas.bind("<Button-1>", self.on_click)

            self.draw_board()

        def draw_board(self):
            self.canvas.delete("all")
            for row in range(ROWS):
                for col in range(COLUMNS):
                    x1 = col * CELL_SIZE + 5
                    y1 = row * CELL_SIZE + 5
                    x2 = x1 + CELL_SIZE - 10
                    y2 = y1 + CELL_SIZE - 10
                    piece = self.board[row][col]
                    fill = piece if piece else "white"
                    self.canvas.create_oval(x1, y1, x2, y2, fill=fill, outline="black")

        def on_click(self, event):
            col = event.x // CELL_SIZE
            if col < 0 or col >= COLUMNS:
                return

            for row in reversed(range(ROWS)):
                if self.board[row][col] == "":
                    self.board[row][col] = PLAYER_COLORS[self.current_player]
                    self.draw_board()

                    if self.check_winner(row, col):
                        color = PLAYER_COLORS[self.current_player].capitalize()
                        messagebox.showinfo("Game Over", f"{color} wins!")
                        self.root.destroy()
                    elif all(self.board[r][c] != "" for r in range(ROWS) for c in range(COLUMNS)):
                        messagebox.showinfo("Game Over", "It's a draw!")
                        self.root.destroy()
                    else:
                        self.current_player = 1 - self.current_player
                    break

        def check_winner(self, row, col):
            color = self.board[row][col]
            return any(
                self.count_in_direction(row, col, dx, dy, color) >= 4
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]
            )

        def count_in_direction(self, row, col, dx, dy, color):
            count = 1
            for dir in [1, -1]:
                r, c = row, col
                while True:
                    r += dy * dir
                    c += dx * dir
                    if 0 <= r < ROWS and 0 <= c < COLUMNS and self.board[r][c] == color:
                        count += 1
                    else:
                        break
            return count

    window = tk.Toplevel()
    ConnectFour(window)

if __name__ == "__main__":
    run_connect_four()