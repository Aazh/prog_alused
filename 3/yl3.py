import random
import math

taringute_arv = int(input("Täringute arv: "))

for i in range(taringute_arv):
    print(math.ceil(random.random() * 6))