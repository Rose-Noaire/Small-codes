import tkinter

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "add":
            result.set(num1 + num2)
        elif operation == "subtract":
            result.set(num1 - num2)
        elif operation == "multiply":
            result.set(num1 * num2)
        elif operation == "divide":
            result.set(num1 / num2 if num2 != 0 else "Error: Division by zero")
        else:
            result.set("Invalid operation")
    except ValueError:
        result.set("Error: Invalid input")

#Main window

app = tkinter.Tk()
app.title("Simple Calculator")

# Create fields for input

entry1 = tkinter.Entry(app)
entry2 = tkinter.Entry(app)
entry1.pack()
entry2.pack()
operation_var = tkinter.StringVar(app)

# Create operation selection
operation_var = tkinter.StringVar(app)
operation_var.set("add")

operation_menu = tkinter.OptionMenu(app, operation_var, "add", "subtract", "multiply", "divide")
operation_menu.pack()

# Nutton to Calculate

calc_button = tkinter.Button(app, text="Calculate", command=calculate)
calc_button.pack()

#Display result

result = tkinter.StringVar()
result_label = tkinter.Label(app, textvariable=result)
result_label.pack()

app.mainloop()
