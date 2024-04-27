from tkinter import Tk, Text, Button

calculation = ""


def add_to_calculator(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def eval_calculations():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = Tk()
root.geometry("300x275")

text_result = Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=5)

btn_1 = Button(root, text="1", command=lambda: add_to_calculator(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = Button(root, text="2", command=lambda: add_to_calculator(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = Button(root, text="3", command=lambda: add_to_calculator(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = Button(root, text="4", command=lambda: add_to_calculator(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = Button(root, text="5", command=lambda: add_to_calculator(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = Button(root, text="6", command=lambda: add_to_calculator(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = Button(root, text="7", command=lambda: add_to_calculator(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = Button(root, text="8", command=lambda: add_to_calculator(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = Button(root, text="9", command=lambda: add_to_calculator(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = Button(root, text="0", command=lambda: add_to_calculator(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_plus = Button(root, text="+", command=lambda: add_to_calculator("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = Button(root, text="-", command=lambda: add_to_calculator("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_multi = Button(root, text="*", command=lambda: add_to_calculator("*"), width=5, font=("Arial", 14))
btn_multi.grid(row=4, column=4)
btn_div = Button(root, text="/", command=lambda: add_to_calculator("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_open = Button(root, text="(", command=lambda: add_to_calculator("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = Button(root, text=")", command=lambda: add_to_calculator(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)
btn_clear = Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equal = Button(root, text="=", command=eval_calculations, width=11, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)


root.mainloop()