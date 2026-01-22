print("hej, Välkommen till min kiosk")
x = input("Du: ")

glass = 20
glass = int(glass)
varmkorv = 15
varmkorv = int(varmkorv)
läsk = 15
läsk = int(läsk)
godis = 15
godis = int(godis)

print("Varorna jag har är följande:")
print("Glass för 20 kr")
print("varmkorv för 15 kr")
print("Läsk för 15 kr")
print("Och godis för 20 kr")
print("Vad vill du ha för något?")

y = input()

if y == "godis":
    print("Hur många kg?")
    c = input()
    c = int(c)
    print("Okej, du vill ha", c, "kg godis för", c*20, "kr")
elif y == "glass":
   print("Hur många?")
   c = input()
   c = int(c)
   print("Okej, du vill ha", c, "glass för", c*20, "kr")
elif y == "varmkorv":
   print("Hur många varmkorvar vill du ha?")
   c = input()
   c = int(c)
   print("Okej du vill ha", c, "varmkorvar för", c*15, "kr")
elif y == "läsk":
   print("Hur många?")
   c = input()
   c = int(c)
   print("Okej du vill ha", c, "läskar för", c*15, "kr")
print("Ha en bra dag")