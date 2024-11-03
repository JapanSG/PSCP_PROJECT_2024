'''save'''
import os
import json
PATH = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(PATH,"password.json")

def add_password(website:str, username : str, password : str) -> None:
    '''Add username and password to a file'''
    num = 1
    dct = {}
    if os.path.exists(file_path) and os.path.getsize(file_path):
        with open(file_path,"r") as file:
            dct = json.load(file)
            num = len(dct)+1
    temp = {num: {"website" : website, "username" : username, "password": password}}
    dct.update(temp)
    with open(file_path,"w") as file:
        json.dump(dct, file)

def clear_file() -> None:
    '''Clear all content in a file'''
    open(file_path,"w").close()

def read_file() -> dict:
    '''Read all content in a file'''
    if os.path.exists(file_path) and os.path.getsize(file_path):
        with open(file_path,"r") as file:
            return json.load(file)
    return {}

def get_pass(key:int)->str:
    '''Return username and password at a key'''
    with open(file_path,"r") as file:
        dct = json.load(file)
        return dct[str(key)]

def del_pass(key :int) -> None:
    '''Delete a specific password'''
    if os.path.exists(file_path) and os.path.getsize(file_path):
        with open(file_path, "r") as file:
            dct : dict = json.load(file)
            dct.pop(str(key))
            new_dct = {}
            num = 1
            for key in dct:
                temp = {num : dct[key]}
                new_dct.update(temp)
                num += 1
        with open(file_path, "w") as file:
            json.dump(new_dct, file)
    else: 
        raise Exception

def __main():
    '''Driver Code'''

if __name__ == "__main__":
    __main()
