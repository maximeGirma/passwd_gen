import time
import os


def get_random_list():
    '''
    calcule le temps que le système met à faire un ping X100, crée un tableau avec ce temps, en secondes
    renvoie un float aléatoire tiré de ce tableau
    '''

    time_list=[]
    i = 0
    while i<100:
        time_1 = time.time()
        a = os.system("ping 8.8.8.8 -c 1")
        if a != 0 :
            time.sleep(1)
            continue

        time_list.append(str(time.time() - time_1))
        i += 1
    return time_list



