from random import randint
import time
import os
def get_pseudo_random_int():

    a = 1
    while a != 0:
        x = time.time()
        a = os.system("ping 8.8.8.8 -c 1")
        if a != 0:
            time.sleep(1)
            continue
    return str(time.time()-x)


def random_value(time_list):


    random_list =[]
    i = 0
    while i < 100:

        pseudo_random_int_in_str = get_pseudo_random_int()
        if len(pseudo_random_int_in_str) < 10:
            continue

        key_1 = int(pseudo_random_int_in_str[2])+2
        key_2 = int(pseudo_random_int_in_str[3])+2
        key_3 = int(pseudo_random_int_in_str[4])+2
        key_4 = int(pseudo_random_int_in_str[5])+2
        key_5 = int(pseudo_random_int_in_str[6])+2
        key_6 = int(pseudo_random_int_in_str[7])+2

        if time_list[int(time_list[key_1][key_2]+time_list[key_3][key_4])][int(time_list[key_5][key_6])] == ".":
            continue
        random_list.append(time_list[int(time_list[key_1][key_2]+time_list[key_3][key_4])][int(time_list[key_5][key_6])])
        i += 1
    random_key = "."

    while random_key == ".":

        pseudo_random_int_in_str = get_pseudo_random_int()
        if len(pseudo_random_int_in_str) < 10:
            continue

        key_1 = int(pseudo_random_int_in_str[2]) + 2
        key_2 = int(pseudo_random_int_in_str[3]) + 2
        key_3 = int(pseudo_random_int_in_str[4]) + 2
        key_4 = int(pseudo_random_int_in_str[5]) + 2
        key_5 = int(pseudo_random_int_in_str[6]) + 2
        key_6 = int(pseudo_random_int_in_str[7]) + 2

        random_key = time_list[int(time_list[key_1][key_2]+time_list[key_3][key_4])][int(time_list[key_5][key_6])]

    random_value = 0

    for element in random_list:
        if element == random_key:
            random_value += 1

    return int(random_value / 2)


def random_bool():

    choice = randint(0, 1)
    print(choice)
    if choice == 0:
        return True
    else:
        return False


def random_letter():

    letters_list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return letters_list[randint(0,26)]

