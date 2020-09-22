inimesed = int(input("Inimeste arv: "))
bussikohad = int(input("Bussi kohtade arv: "))
print("Bussi kohtade arv: " + str(bussikohad))
bussid = inimesed // bussikohad
print("Busside arv: " + str(bussid))
mahajaanud = bussid * bussikohad
print("Bussile mahtunud inimeste arv: " + str(mahajaanud))
jaak = inimesed % bussikohad
print("Mahajäänud inimeste arv: " + str(jaak))
