students = ["Linus", "Anton", "Kurt"]
"""
print(students[0])

students.append("Johan") #lägga till saker i listan
print(students)

students.insert(1, "Erik") #lägger till en sak i listan fast på en exakt position / plats
print(students)

students.remove("Johan") #tar bort en sak från listan enligt namn
print(students)
"""
students.pop(1)
print(students) #tar bort en sak i listan enligt position


#komma åt innehållet
for student in students: #printar ut listan i order från 0 - slutet
    print(student)

numbers = [10, 77, 53, 24]

#ändrar innehållet
for i in range(len(numbers)): #går igenom alla nummer i listan och adderar 10
    numbers[i] += 10 

print(numbers)