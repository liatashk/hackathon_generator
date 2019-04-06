import random
from typing import List
from typing import Dict
from typing import ByteString

def read_list_from_file(file_name) -> List:
    f = open(file_name)
    list = []
    for x in f:
        list.append(x.strip())
    f.close()
    return list


def rand_select_elm(who_list, what_list, when_list) -> Dict:
    hack_dict = {}
    hack_dict["Who"] = who_list[random.randint(0, len(who_list) - 1)]
    hack_dict["What"] = what_list[random.randint(0, len(what_list) - 1)]
    hack_dict["When"] = when_list[random.randint(0, len(when_list) - 1)]
    return hack_dict


def create_sentence(dict) -> ByteString:
    str=""
    for x in dict:
        str=str+x+":"+dict.get(x)+" "
    return str

i = 1
while i < 20:
    print(create_sentence(
        rand_select_elm(read_list_from_file("who.txt"), read_list_from_file("what.txt"), read_list_from_file("when.txt"))))
    i = i + 1