# ru->en convertor
# if you wrote in ru KB layout but needed to write in en KB layout
en_alph = "abcdefghijklmnopqrstuvwxyz 1234567890.,?!#*" # we need spaces :}
ru_alph = "фисвуапршолдьтщзйкыегмцчня 1234567890.,?!#*" # this is not ru alph but it is en alph in ru keyboard layout

a = input()
enstr = ""
for i in range(len(a)):
    countd =  ru_alph.index(a[i])
    enstr += en_alph[countd]

print(enstr)

# this is currently in BETA 
# TODO:
# - Aff function instead of direct code
# - Add reverced mode en->ru (so it will be en<->ru)
