fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in fail:
    vastuvoetud.append(int(rida))
fail.close()

aasta = int(input("Vastuvõetute arv millisel aastal?: "))

if 2010 < aasta < 2020:
    print("Aastal " + str(aasta) + " võeti vastu " +str(vastuvoetud[aasta - 2011]) + " inimest.")
else:
    raise Exception("Aasta pole andmete hulgas.")
