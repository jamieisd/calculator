import tkinter 

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#D4D4D2" 
colore_black = "#1C1C1C"
colore_dark_gray = "#505050"
colore_orange = "#FF9500"
color_white = "#FFFFFF"


window = tkinter.Tk()
window.title("Taschenrechner")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0",  font=("Arial", 45), bg=colore_black, fg=color_white, anchor="e", width=column_count)


label.grid(row=0, column=0, columnspan=column_count, sticky="we")


for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=colore_black, bg=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, bg=colore_orange)
        else:
            button.config(foreground=color_white, bg=colore_dark_gray)
        button.grid(row=row+1, column=column)

frame.pack()

A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    B = None
    operator = None
    label["text"] = "0"


def remove_zero_decimal(num):
    if num % 1 == 0:
        return str(int(num))
    else:
        return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
         if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                      label["text"] = remove_zero_decimal(numA / numB)


         elif value in "+-×÷":
            if operator is not None:
                A = label["text"]
                label["text"] = "0"
                B = "0" 

            operator = value


            A = label["text"]
            operator = value
            label["text"] = "0"
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
            
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

        if value == ".":
            if value not in label["text"]:
                label["text"] += value




    elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                    label["text"] += value



window.update




window.mainloop()