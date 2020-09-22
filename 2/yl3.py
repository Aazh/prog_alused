vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ").lower()
treeningutuup = input("Sisestage treeningu tüüp: ")
if sugu == "m":
    max_pulsisagedus = 220 - vanus
elif sugu == "n":
    max_pulsisagedus = 206 - vanus * 0.88

if treeningutuup == "1":
    vahem = 0.5 * max_pulsisagedus
    suurem = 0.7 * max_pulsisagedus
elif treeningutuup == "2":
    vahem = 0.7 * max_pulsisagedus
    suurem = 0.8 * max_pulsisagedus
elif treeningutuup == "3":
    vahem = 0.8 * max_pulsisagedus
    suurem = 0.87 * max_pulsisagedus

print("Pulsisagedus peaks olema vahemikus " + str(round(vahem)) + " kuni " + str(round(suurem)) + ".")
