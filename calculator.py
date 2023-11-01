import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result_label.config(text="Error: Division by zero")
            return
    else:
        result_label.config(text="Error: Invalid operation")
        return
    
    result_label.config(text="Result: " + str(result))

app = tk.Tk()
app.title("Simple Calculator")

entry1 = tk.Entry(app)
entry1.pack()

operation_var = tk.StringVar()
operation_var.set('+')
operation_option = tk.OptionMenu(app, operation_var, '+', '-', '*', '/')
operation_option.pack()

entry2 = tk.Entry(app)
entry2.pack()

calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
