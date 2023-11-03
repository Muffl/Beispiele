#Lottozahlen Generator als Python code als Gui

import random
from tkinter import *
 
# Erstelle ein Fenster
fenster = Tk()
fenster.title("Lottozahlen Generator")
fenster.geometry("400x200")
 
# Erstelle eine Funktion, um die Lottozahlen zu generieren 
def lotto_zahlen(): 
    zahlen = [] 

    # Generiere 6 verschiedene Zahlen zwischen 1 und 49  
    while len(zahlen) < 6: 
        num = random.randint(1, 49) 

        # Überprüfe, ob die Zahl schon vorhanden ist  
        if num not in zahlen: 
            zahlen.append(num) 

    # Sortiere die Zahlen in aufsteigender Reihenfolge  
    zahlen.sort() 

    # Zeige die generierten Zahlen im Label an  
    label_lotto_zahlen["text"] = str(zahlen)  

     # Erstelle den Button "Generiere Lottozahlen"  
btn_generate = Button(fenster, text="Generiere Lottozahlen", command=lotto_zahlen)  
btn_generate.pack()  

 # Erstelle das Label für die Lottozahlenausgabe  
label_lotto_zahlen = Label(fenster, font=("Helvetica", 16))  
label_lotto_zahlen.pack()  

 # Starte den Hauptloop des Fensters  
fenster.mainloop()