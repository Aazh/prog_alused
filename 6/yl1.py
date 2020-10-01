def banner(reklaamlause: str):
    return reklaamlause.upper()


kordused = int(input("Mitu korda soovite reklaamlauset kuvada? "))
reklaamlause = input("Sisestage reklaamlause: ")

for i in range(kordused):
    print(banner(reklaamlause))
