import datetime

#print((end_date - start_date).days)

print("år, månad, dag")
print("Skriv precis som ovan med comma fast riktigt start datum")
start_date = float(datetime.datetime(input()))

print("år, månad, dag")
print("Som innan ")
end_date = datetime.datetime(2025, 10, 10)

#hur fan lägger man till datetime??? datetime.datetime(input()) fungerar inte aaaaaaaaaaaaa


print("Vad var din elmätare på från början?")
meterstart = int(input())

print("Vad var din elmätare på på slutet?")
meterend  = int(input())

print("Vad är din dagskostnad?")
daysomething = int(input()) 

print("Vad var din kwh?")
kwh = float(input())

Total = 1.25 * meterend - 1.25 * meterstart + 1.25 * daysomething * 30 + 1.25 * kwh * 720

print(Total, "kr är din elräkning från", start_date, "till", end_date, "inklusive moms.")