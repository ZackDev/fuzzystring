import re, random, string, os

supported_types = ['a', 'n', 's']
count_types = []

def fuzzyfy(types, length):

    #check type and length parameters for validity
    try:
        val = int(length)
    except:
        return None

    if types == '' or types == "":
        return None

    elif length < 1:
        return None

    for type in types:
        try:
            supported_types.index(type)
        except:
            return None

    for type in types:
        type_occured = False
        for counter in count_types:
            if counter[0] == type:
                counter[1] += 1
                type_occured = True
        if type_occured == False:
            count_types.append([type, 1])

    for counter in count_types:
        if counter[1] > 1:
            return None

    #build fuzzy string
    fuzzystr = str("")
    for i in range(0,length):
        fuzzystr += str(_type_to_char(random.choice(types)))

    #check fuzzy string for expected legth
    if len(fuzzystr) == length:
        return fuzzystr
    else:
        return None

def _type_to_char(type):
    #returns character for a given type
    if type == "a":
        return(random.choice(string.ascii_lowercase + string.ascii_uppercase))
    elif type == "n":
        return(random.choice(string.digits))
    elif type == "s":
        return(random.choice(string.punctuation))
    else:
        return str("")

def test():
    print(fuzzyfy('ab', 2))
    print(fuzzyfy('ans', 2))
    print(fuzzyfy('', 0))
    print(fuzzyfy('ans', 5))
    print(fuzzyfy('xxansxx', 99))
    print(fuzzyfy('ansans', 9))
    print(fuzzyfy('ans', 'a'))
    print(fuzzyfy('an', -1))
    print(fuzzyfy('ans', 11))
    print(fuzzyfy('an', 1))
    print(fuzzyfy('san', 5))

if __name__ == '__main__':
    s = fuzzyfy('ans', 10)
    print(s)
