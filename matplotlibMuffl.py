

import matplotlib.pyplot as plt
import numpy as np


# Funktion x^x

wert = [0]
for i in range(1, 64, 1):
    wert.append(i**i)

print(wert)
plt.plot(range(len(wert)), wert, color="green")
plt.xscale("log")
plt.yscale("log")
plt.title("Funktion y^y")
plt.show()
print()


# Funktion y^2

wert = [0]
for i in range(1, 64, 1):
    wert.append(i**2)

print(wert)
plt.plot(range(len(wert)), wert, color="red")
# plt.xscale("log")
# plt.yscale("log")
plt.title("Funktion y^2")
plt.show()
print()




# Reiskörner berechnen

wert = [1]
erg = 1
Gesamtgew = 0
Gesamtanzahl = 0
for i in range(1, 65, 1):
    erg = erg * 2
    if i == 64:
        erg = erg -1
    wert.append(erg)

    Gesamtgew = Gesamtgew + erg * 0.02/1000/1000
    Gesamtanzahl = Gesamtanzahl +erg

    print("Verdopplung Nr: ", i, wert)
print("Gesamtgewicht: ", Gesamtgew, "Tonnen")
print("Gesamtanzahl: ", Gesamtanzahl, "Reiskörner")

plt.plot(range(len(wert)), wert, color="blue")
# plt.xscale("log")
plt.yscale("log")
plt.title("Reiskörner")

plt.show()
print()


# Funktion tan

wert = [0]

for i in range(1, 64, 1):

    wert.append(np.tan(i))

print(wert)
plt.plot(range(len(wert)), wert, color="brown")
# plt.xscale("log")
# plt.yscale("log")
plt.title("Funktion tan")
plt.show()
print()



# Funktion cos

wert = [0]

for i in range(1, 64, 1):

    wert.append(np.cos(i))

print(wert)
plt.plot(range(len(wert)), wert, color="purple")
# plt.xscale("log")
# plt.yscale("log")
plt.title("Funktion cos")
plt.show()
print()


# Funktion sin

wert = [0]

for i in range(1, 64, 1):

    wert.append(np.sin(i))

print(wert)
plt.plot(range(len(wert)), wert, color="orange")
# plt.xscale("log")
# plt.yscale("log")
plt.title("Funktion sin")
plt.show()
print()


# Funktion cos*tan*sin

wert = [0]

for i in range(1, 64, 1):

    wert.append(np.cos(i)*np.tan(i)*np.sin(i))

print(wert)
plt.plot(range(len(wert)), wert, color="black")
# plt.xscale("log")
# plt.yscale("log")
plt.title("Funktion cos*tan*sin")
plt.show()
print()

# Funktion Eulersche Zahl

wert = [0]
erg = 0
for i in range(1, 64, 1):

    erg = (1+(1/i))**i


    wert.append(erg)

print(wert)
plt.plot(range(len(wert)), wert, color="pink")
# plt.xscale("log")
# plt.yscale("log")
plt.title("Funktion Eulersche Zahl")
plt.show()
print()
