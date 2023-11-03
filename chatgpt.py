import random
import tkinter as tk
from tkinter import messagebox

def generate_lotto_numbers():
    all_draws = ""
    for _ in range(20):
        numbers = random.sample(range(1, 50), 6)
        numbers.sort()
        draw = ", ".join(str(num) for num in numbers)
        all_draws += f"{draw}\n"

    messagebox.showinfo("Lottozahlen", f"Ihre Lottozahlen sind:\n\n{all_draws}")

def exit_program():
    window.destroy()

window = tk.Tk()
window.title("Lottozahlen Generator")
window.geometry("300x200")

btn_generate = tk.Button(window, text="Lottozahlen generieren", command=generate_lotto_numbers)
btn_generate.pack(pady=20)

btn_exit = tk.Button(window, text="Beenden", command=exit_program)
btn_exit.pack()

window.mainloop()
