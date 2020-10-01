fail = open("konto.txt", encoding="UTF-8")
kontod = []
for rida in fail:
    kontod.append(rida.strip())
fail.close()

for konto in kontod:
    if float(konto) >= 0:
        print(konto)
