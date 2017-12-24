'''
MaximeGirma
22/12/2017
version0.5
Generateur de mot de passe pseudo aléatoires. Ce programme utilise la fonction randint()
et le temps que met le système a effectuer un ping sur google.com pour generer des mots de passe pseudo aléatoires
MAJ possibles: se passer totalement de randint() mais c'est long et un peu chiant
                reduire la range de random_value()
                reduire l'usage du ping ( un seul tableau)
'''

import time
import os
from random import randint

from src.random_gen import get_random_list
from src.get_things import get_pseudo_random_int
from src.get_things import random_letter
from src.get_things import random_bool
from src.get_things import random_value

rdm_list = get_random_list()

nb_letter = random_value(rdm_list)
nb_number = random_value(rdm_list)
nb_maj = random_value(rdm_list)
password_list = []

print(nb_letter,nb_maj,nb_number)
boucle_check=[0,0,0,0]

while (nb_letter > 0) or (nb_maj > 0) or (nb_number > 0):
    print(boucle_check)
    random_condition = random_bool()
    random_condition_2 = random_bool()

    if random_condition is True and nb_number > 0:
        try:
            password_list.append(str(random_value(rdm_list)))
            nb_number -= 1
            boucle_check[1] = boucle_check[1] + 1
        except IndexError:
            continue

    elif random_condition is False and random_condition_2 is True and nb_letter > 0:
        try:
            password_list.append(random_letter())
            nb_letter -= 1
            boucle_check[2] = boucle_check[2] + 1
        except IndexError:
            continue

    elif random_condition is not True and random_condition_2 is False and nb_maj > 0:
        try:
            password_list.append(random_letter().upper())
            nb_maj -= 1
            boucle_check[3] = boucle_check[3] + 1
        except IndexError:
            continue
    boucle_check[0] = boucle_check[0] + 1

password = ""

for element in password_list:
    password += element

print(password)


