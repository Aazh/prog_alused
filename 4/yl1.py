nimed = input("Sisesta eesnimi ja perekonnanimi: ").split(" ")

vastus = []
for nimi in nimed:
    vastus.append(nimi.lower().capitalize())
print(" ".join(vastus))
