from typing import List
from typing import Dict

def read_list_from_file(file_name) -> Dict:
    f = open(file_name)
    list = []
    dict={}
    for x in f:
        list.append(x.strip())
    f.close()
    i=0
    while i< len(list):
       dict[list[i]] = list[i+1]
       i=i+2
    return dict


def is_verified(vin, password) -> bool:
    dict = read_list_from_file("vin_pass.txt")
    print(dict)
    ans=False
    if(dict.get(vin)== password):
        ans=True
    else:
        ans=False
    print(ans)
    return(ans)

is_verified("77","blabla")