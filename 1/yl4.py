nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
trahv = min(190, (tegelik_kiirus - lubatud_kiirus) * 3)
vastus = nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot."
print(vastus)
