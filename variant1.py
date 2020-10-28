import random


def inimeste_arv(naiskondade_arv: int, tugiisikute_arv: int) -> int:
    return naiskondade_arv * (22 + tugiisikute_arv)


def genereeri_turniiride_naiskondade_arvud(arv: int) -> list:
    naiskondade_arvud = []
    for i in range(arv):
        naiskondade_arvud.append(random.randint(10, 30))
    return naiskondade_arvud


def loenda_turniire(turniiride_naiskondade_arvud: list):
    turniiride_inimeste_summa = 0
    for naiskondade_arv in turniiride_naiskondade_arvud:
        if naiskondade_arv < 15:
            tugiisikute_arv = 10
        else:
            tugiisikute_arv = 8
        inimeste_kogus = inimeste_arv(naiskondade_arv, tugiisikute_arv)
        turniiride_inimeste_summa += inimeste_kogus
        print("Turniiril oli {} naiskondi ja vastavalt inimesi: {}".format(naiskondade_arv, inimeste_kogus))
    print("Kokku oli kõigil turniiridel inimesi: {}".format(turniiride_inimeste_summa))


def main():
    asukoht = input("Kus toimisid maailmameistrivõistlused: ")
    print("Turniirid toimusid {}".format(asukoht))
    turniiride_arv = int(input("Kui palju turniiri toimus: "))

    # turniiri naiskondade arvude genereerimine ja nendest välja loendamine on eraldatud oma funktsioonidesse.
    turniiride_naiskondade_arvud = genereeri_turniiride_naiskondade_arvud(turniiride_arv)
    loenda_turniire(turniiride_naiskondade_arvud)


main()
