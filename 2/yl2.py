perekonnanimi = input("Sisestage leedu perekonnanimi: ")
if perekonnanimi[-2:] == "ne":
    print("Abielus")
elif perekonnanimi[-2:] == "te":
    print("Vallaline")
elif perekonnanimi[-1:] == "e":
    print("Määramata")
else:
    print("Pole ilmselt leedulanna perekonnanimi")