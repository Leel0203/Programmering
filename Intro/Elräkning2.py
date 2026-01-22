from datetime import datetime

TAX = 1.25

print("Ange ett startdatum: YYYY-MM-DD")
start_date = input()
print("Ange ett slutdatum: YYYY-MM-DD")
end_date = input()
print("Ange elmätarens startvärde:")
meterstart = float(input())
print("Ange elmätarens slutvärde:")
meterend = float(input())
print("Ange dagspriset:")
daysomethingprice = float(input())
print("Ange kwh:")
kwh = float(input())

date_format = "%Y-%m-%d"
start_date2 = datetime.strptime(start_date, date_format)
end_date2 = datetime.strptime(end_date, date_format)

Number_of_days = (end_date2 - start_date2).days

MeterTotal = meterend - meterstart

Electricity = kwh * MeterTotal
DayPaymentorwhatever = daysomethingprice * Number_of_days
X = Electricity + DayPaymentorwhatever
TotalMoneys = X * TAX

print("Elräkning")
print("Din totala elräkning från datum", start_date, "till", end_date, "är", TotalMoneys, "kr.")

#Jag fastnade så jävla hårt på hur jag skulle använda datetime 
#och kom inte på något så rad 16-20 och "from datetime" i rad 1
#kan jag inte ta äran för
#jag skriver om koden själv om det behövs
#3 timmar sömn inte rekommenderat