import tkinter as tk
import random

def run_magic_8_ball():
    messages = [
        'It is certain', 'It is decidedly so', 'Yes definitely',
        'Reply hazy, try again', 'Ask again later',
        'Concentrate and ask again', 'My reply is no',
        'Outlook not so good', 'Very doubtful'
    ]

    def get_answer():
        answer.set(random.choice(messages))

    window = tk.Toplevel()
    window.title("Magic 8 Ball")

    tk.Label(window, text="Ask a question:").pack(pady=10)
    entry = tk.Entry(window, width=40)
    entry.pack(pady=5)

    tk.Button(window, text="Shake the Ball", command=get_answer).pack(pady=10)

    answer = tk.StringVar()
    tk.Label(window, textvariable=answer, font=("Arial", 14), wraplength=250).pack(pady=20)

if __name__ == "__main__":
    run_magic_8_ball()