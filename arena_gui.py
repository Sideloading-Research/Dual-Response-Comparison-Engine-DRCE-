# arena_gui.py

import tkinter as tk
from tkinter import messagebox
from parse_markdown import parse_markdown_answers
import json
import random

class ArenaApp:
    def __init__(self, root, original, generated, output_file):
        self.root = root
        self.questions = list(original.keys())
        random.shuffle(self.questions)
        self.original = original
        self.generated = generated
        self.output_file = output_file
        self.scores = { "original": 1500, "generated": 1500 }

        self.current = 0
        self.build_gui()

    def build_gui(self):
        self.root.title("Arena Elo Rater")
        self.question_label = tk.Label(self.root, text="", wraplength=600, font=("Arial", 12, "bold"))
        self.answer1 = tk.Text(self.root, height=5, width=80)
        self.answer2 = tk.Text(self.root, height=5, width=80)
        self.btn_a = tk.Button(self.root, text="Select A", command=lambda: self.rate("a"))
        self.btn_b = tk.Button(self.root, text="Select B", command=lambda: self.rate("b"))

        self.question_label.pack(pady=10)
        self.answer1.pack()
        self.answer2.pack()
        self.btn_a.pack(side=tk.LEFT, padx=20, pady=10)
        self.btn_b.pack(side=tk.RIGHT, padx=20, pady=10)

        self.load_question()

    def load_question(self):
        if self.current >= len(self.questions):
            with open(self.output_file, "w") as f:
                json.dump(self.scores, f, indent=2)
            messagebox.showinfo("Done", f"All questions rated.\nScores: {self.scores}")
            self.root.quit()
            return

        q = self.questions[self.current]
        a1 = self.original[q]
        a2 = self.generated[q]

        if random.choice([True, False]):
            self.answer_a = a1
            self.answer_b = a2
            self.label_a = "original"
            self.label_b = "generated"
        else:
            self.answer_a = a2
            self.answer_b = a1
            self.label_a = "generated"
            self.label_b = "original"

        self.question_label.config(text=f"Q{self.current+1}: {q}")
        self.answer1.delete("1.0", tk.END)
        self.answer2.delete("1.0", tk.END)
        self.answer1.insert(tk.END, self.answer_a)
        self.answer2.insert(tk.END, self.answer_b)

    def rate(self, winner):
        loser = "b" if winner == "a" else "a"
        winner_label = self.label_a if winner == "a" else self.label_b
        loser_label = self.label_b if winner == "a" else self.label_a
        self.update_elo(winner_label, loser_label)
        self.current += 1
        self.load_question()

    def update_elo(self, winner, loser, k=32):
        Ra = self.scores[winner]
        Rb = self.scores[loser]
        Ea = 1 / (1 + 10 ** ((Rb - Ra) / 400))
        self.scores[winner] += int(k * (1 - Ea))
        self.scores[loser] -= int(k * (1 - Ea))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", required=True, help="Original file (markdown)")
    parser.add_argument("--b", required=True, help="Generated file (markdown)")
    parser.add_argument("--output", default="elo_scores.json")
    args = parser.parse_args()

    a_data = parse_markdown_answers(args.a)
    b_data = parse_markdown_answers(args.b)

    root = tk.Tk()
    app = ArenaApp(root, a_data, b_data, args.output)
    root.mainloop()
