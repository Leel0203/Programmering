while True:
    results = ""
    sentence = input("Enter a sentence: ")  #kanske ska sätta i en while True loop eller inte
    if not sentence.isalpha():
        continue

    while True:
        try:
            caesar_encryption_code = int(input("Enter how many spots you want to move this sentence forward or back: "))
            break
        except ValueError:
            print("Enter a number. Negative or not.")
            continue

    for i in sentence:
        if i.islower():
            start = ord("a")    #man kan använda index() med en variabel som är hela alfabetet
        else:
            start = ord("A")

        position = ord(i) - start
        new_position = (position + caesar_encryption_code) % 26 #har inte med å, ä, ö
        new_sentence = chr(new_position + start)
        results += new_sentence 
        #ngl hade glömt bort både ord och chr så mestadels av innehållet av denna for loop är stulet

    print(results)