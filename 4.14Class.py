import tkinter as tk
import random


root = tk.Tk()
root.title("D20 Roller")
root.geometry("1100x800")


result_label = tk.Label(root, text="", font=("BD_MicronFont", 48), width=20, borderwidth=2, relief="solid")
result_label.pack(pady=20)


def roll_d20():
    roll = random.randint(1, 20)
    result_label.config(text=str(roll))

    if roll < 10:
        root.config(bg="white")
        result_label.config(bg="white", fg="black")
    else:
        root.config(bg="red")
        result_label.config(bg="red", fg="white")


roll_button = tk.Button(root, text="Roll!", font=("Helvetica", 16), command=roll_d20)
roll_button.pack(pady=10) 


root.mainloop()