def kuu_nimi(kuu: int) -> str:
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni",
            "juuli", "august", "september", "oktoober", "november",
            "detsember"]
    return kuud[kuu]


def kuupäev_sõnena(kuu: str) -> str:
    kuu_osad = kuu.split(".")
    return "{}. {} {}. a".format(kuu_osad[0], kuu_nimi(int(kuu_osad[1]) - 1), kuu_osad[2])


sisend_kuupaev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

print(kuupäev_sõnena(sisend_kuupaev))
