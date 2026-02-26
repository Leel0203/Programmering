print("Hur gammal är du?")

age = input()
age = int(age)

if age <= 7:
    print("Du får betala 21 kr (0-7)")
elif age <= 19:
    print("Du får betala 21 kr här också (7-19)")
elif age >= 20 and age <= 64:
    print("Du får betala 32kr (20-64)")
elif age >=65:
    print("Du får betala 21kr, för att du är gammal (65+)")