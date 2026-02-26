swedish_to_english = {
    "ladugård" : "barn", 
    "fönster" : "window", 
    "konst" : "art"
}

#print(swedish_to_english["konst"])
#swedish_to_english["fönster"] = "hallå"
#print(swedish_to_english["fönster"])

volvo = {
    "model" : "740",
    "electric" : False,
    "year" : "1984",
    "colors" : ["brun", "grå"]
}

volvo["is broken "] = True
volvo.pop("electric")

print(f"Volvo {volvo['model']} Årsmodel {volvo['year']}")