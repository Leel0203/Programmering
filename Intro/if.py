print("Hur gammal är du?")

age = input()
age = int(age)

if age < 18:
    print("du är ett barn")
elif age == 18:
    print("Du är 18")
elif age >= 18 and age < 50:
    print("Du är vuxen")
elif age >= 50 and age > 99:
    print("Du är gammal")
elif age >= 99: #kommer inte aktiveras
    print("Bror du är uråldrig")
else: 
    print("Jag vet inte")
#denna kod är på något sätt trasig och fungerar inte när den är i folderna (intro) 
#osäker på vad jag menade med detta