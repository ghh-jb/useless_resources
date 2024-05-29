# ru->en convertor
# if you wrote in ru KB layout but needed to write in en KB layout
# ru->en convertor

# ru->en convertor

# ru->en convertor

def ru_to_en_and_rev(a:str, mode:str) -> str: 
    ru_alph = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя .,!?" 
    en_alph = "f,dult`;pbrkvyjghcnea[wxio]sm'.z .,!?" # orient to .ru alphabet
    revercestr = ""
    if mode == "ru->en":
        for i in range(len(a)):
            countd =  ru_alph.index(a[i])
            revercestr += en_alph[countd]
        return revercestr
    
    elif mode == "en->ru":
        for i in range(len(a)):
            countd = en_alph.index(a[i])
            revercestr += ru_alph[countd]
        return revercestr
    
    
    
print("[+] Enter convertor mode:")
mode = input()
if mode != "en->ru" and mode != "ru->en":
    print("[-] FAIL: enter CORRECT mode...")
    exit()
print("[+] Enter your strunt_to_convert:")
string = input()
print(ru_to_en_and_rev(string, mode))

# this is currently in BETA
# TODO:
# - Aff function instead of direct code /*DONE*/
# - Add reverced mode en->ru (so it will be en<->ru) /*DONE*/
# - Now can be released
