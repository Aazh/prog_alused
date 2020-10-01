def eelarve(kulaliste_arv: int):
    return 10 * kulaliste_arv + 55


kutsutud = int(input("Mitu inimest on kutsutud? "))
tulejad = int(input("Mitu inimest tuleb? "))

print("Maksimaalne eelarve: {} eurot".format(eelarve(kutsutud)))
print("Minimaalne eelarve: {} eurot".format(eelarve(tulejad)))