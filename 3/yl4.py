import random

tahtjate_arv = int(input("Mitu pöialpoissi tahab õunu? "))
ounad = 14

for i in range(tahtjate_arv):
    arv = random.randint(1, 2)
    print(arv)
    ounad -= arv
print("Limivalgekesele jäi " + str(ounad))