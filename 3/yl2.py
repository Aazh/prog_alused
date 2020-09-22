ringide_arv = int(input("Sisesta ringide arv: "))
porgand_arv = 0

i = 0
while i < ringide_arv:
    i += 1
    if i % 2 == 0:
        porgand_arv += i

print("Porgandite koguarv on " + str(porgand_arv) + ".")