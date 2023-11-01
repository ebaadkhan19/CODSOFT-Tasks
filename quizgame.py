import tkinter as tk
from tkinter import messagebox

class FootballQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Football Quiz")

        self.question_number = 0
        self.score = 0

        self.questions = [
            {
                'question': 'Which country won the FIFA World Cup in 2018?',
                'options': ['France', 'Brazil', 'Germany', 'Argentina'],
                'correct_answer': 'France'
            },
            {
                'question': 'Who is the all-time top scorer in FIFA World Cup history?',
                'options': ['Pele', 'Lionel Messi', 'Miroslav Klose', 'Cristiano Ronaldo'],
                'correct_answer': 'Miroslav Klose'
            },
            {
                'question': 'Which player has the most Ballon d\'Or awards?',
                'options': ['Lionel Messi', 'Cristiano Ronaldo', 'Michel Platini', 'Marco van Basten'],
                'correct_answer': 'Lionel Messi'
            }
        ]

        self.question_label = tk.Label(root, text='')
        self.question_label.pack()

        self.option_var = tk.StringVar()
        self.radio_buttons = []

        for i in range(4):
            radio_button = tk.Radiobutton(root, text='', variable=self.option_var, value='', command=self.check_answer)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.next_button = tk.Button(root, text='Next', command=self.next_question, state=tk.DISABLED)
        self.next_button.pack()

        self.result_button = tk.Button(root, text='Show Results', command=self.show_results, state=tk.DISABLED)
        self.result_button.pack()

        self.results_label = tk.Label(root, text='')
        self.results_label.pack()

        self.next_question()

    def next_question(self):
        if self.question_number < len(self.questions):
            question = self.questions[self.question_number]
            self.question_label.config(text=question['question'])

            for i in range(4):
                self.radio_buttons[i].config(text=question['options'][i])
                self.radio_buttons[i]['value'] = question['options'][i]

            self.option_var.set('')
            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo('Quiz Complete', f'Your score: {self.score}/{len(self.questions)}')
            self.next_button.config(state=tk.DISABLED)
            self.result_button.config(state=tk.NORMAL)

    def check_answer(self):
        selected_option = self.option_var.get()
        correct_answer = self.questions[self.question_number]['correct_answer']

        if selected_option == correct_answer:
            self.score += 1

        self.question_number += 1
        self.next_button.config(state=tk.NORMAL)

    def show_results(self):
        self.results_label.config(text=f'Your score: {self.score}/{len(self.questions)}')
        self.result_button.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    app = FootballQuiz(root)
    root.mainloop()
