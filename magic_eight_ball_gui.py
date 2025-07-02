import tkinter as tk
import random

def run_magic_eight_ball():
    messages = [
        'It is certain', 'It is decidedly so', 'Yes, definitely',
        'Reply hazy, try again', 'Ask again later',
        'Concentrate and ask again', 'My reply is no',
        'Outlook not so good', 'Very doubtful'
    ]

    def get_answer():
        question = entry.get().strip()
        if not question:
            answer.set("Please enter a question!")
        else:
            answer.set(random.choice(messages))

    window = tk.Toplevel()
    window.title("Magic 8 Ball")
    window.geometry("350x250")
    window.lift()
    window.focus_force()
    window.grab_set()

    tk.Label(window, text="Ask a question:", font=("Arial", 12)).pack(pady=10)

    entry = tk.Entry(window, width=40, font=("Arial", 12))
    entry.pack(pady=5)

    tk.Button(window, text="Shake the Ball", command=get_answer).pack(pady=10)

    answer = tk.StringVar()
    tk.Label(window, textvariable=answer, font=("Arial", 14), wraplength=300, justify="center").pack(pady=20)

if __name__ == "__main__":
    run_magic_eight_ball()