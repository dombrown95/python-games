import chess
import chess.svg

def print_board(board):
    print(board.unicode())

def main():
    board = chess.Board()

    print("Welcome to Python Chess!")
    while not board.is_game_over():
        print_board(board)
        print(f"\n{('White' if board.turn else 'Black')}'s move")

        move_input = input("Enter your move (e.g., e2e4): ").strip()

        try:
            move = chess.Move.from_uci(move_input)
            if move in board.legal_moves:
                board.push(move)
            else:
                print("Illegal move. Try again.")
        except ValueError:
            print("Invalid move format. Try again.")

    print_board(board)
    result = board.result()
    print(f"Game Over. Result: {result}")

if __name__ == "__main__":
    main()