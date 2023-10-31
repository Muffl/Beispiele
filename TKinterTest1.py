import tkinter as tk

root = tk.Tk()

root.title("Hallo Muffl")

root.geometry("800x400")

label1 = tk.Label(root, text = "Hallo Welt ")
label1.pack()
label1 = tk.Label(root, text="Red Sun", bg="red", fg="white")
label1.pack()
label1 = tk.Label(root, text="Green Grass", bg="green", fg="black")
label1.pack()
label1 = tk.Label(root, text="Blue Sky", bg="blue", fg="red")
label1.pack()



root.mainloop()
