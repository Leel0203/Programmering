#mening = sentence.append(input("Skriv en mening på svenska: ")) #trodde lowk inte detta skulle funka

mening = input("Skriv en mening på svenska: ")

print(mening.replace('å', 'a').replace('Å', 'A').replace('ä', 'a').replace('Ä', 'A').replace('ö', 'o').replace('Ö', 'O'))

#Det enda ja stal här var replace() okej, vilket tbf är typ 90% av koden