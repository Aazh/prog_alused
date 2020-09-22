suurus = float(input("Sisestage kirja suurus: "))
pealkiri = input("Sisestage kirja teema pealkiri: ")
fail = input("Kas kirjaga on kaasas fail?: ")

if (suurus > 1 and fail == "jah") or (pealkiri == ""):
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")
