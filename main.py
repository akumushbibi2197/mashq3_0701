#1-misol
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

ikkinchi = a + b + c - max(a, b, c) - min(a, b, c)
print("Ikkinchi katta son:", ikkinchi)

#2-misol
h1 = int(input("1-vaqt soati: "))
m1 = int(input("1-vaqt minuti: "))

h2 = int(input("2-vaqt soati: "))
m2 = int(input("2-vaqt minuti: "))

t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

farq = abs(t2 - t1)
print("Farq (daqiqada):", farq)

#3-misol
parol = input("Parol kiriting: ")

if len(parol) >= 8:
    print("Parol uzunligi yetarli")
else:
    print("Parol juda qisqa")

#4-misol
n = input("4 xonali son kiriting: ")

if len(n) == 4 and len(set(n)) == 4:
    print("Barcha raqamlar turli")
else:
    print("Raqamlar bir xil yoki son 4 xonali emas")

#5-misol
kun = int(input("Kun: "))
oy = int(input("Oy: "))

if 1 <= oy <= 12 and 1 <= kun <= 31:
    print("Sana to‘g‘ri kiritilgan")
else:
    print("Sana noto‘g‘ri")
