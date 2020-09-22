import random
loos = input('Kas soovite istekohta ise valida ("ise") või loosida ("loos")? ')

if loos == "ise":
    koht = input('Kas soovite istuda akna ääres ("aken") või mitte ("muu")? ')
    vastus = "Valisite ise. "

elif loos == "loos":
    if random.randint(1, 3) == 1:
        koht = "aken"
    else:
        koht = "muu"
    vastus = "Istekoht loositi. "

if koht == "aken":
    vastus += "Aknakoht"
elif koht == "muu":
    vastus += "Vahekäigukoht"

print(vastus)