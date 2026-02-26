import datetime

start_date = input("Ange ett startdatum i formatet YYYY-MM-DD: ")
end_date = input("Ange ett slutdatum i formatet YYYY-MM-DD: ")

date_format = "%Y-%m-%d"
start_date2 = datetime.datetime(start_date, date_format)
end_date2 = datetime.datetime(end_date, date_format)

print() #kom inte ihåg va ja höll på med.