__author__ = 'ZackDev'

#generate a string consisting of:
#-alphabet characters - a
#-numerals - n
#-special characters - s

#return None if input is invalid

import re, random, string

regexstr = "a{0,1}n{0,1}s{0,1}|\
            a{0,1}s{0,1}n{0,1}|\
            s{0,1}n{0,1}a{0,1}|\
            s{0,1}a{0,1}n{0,1}|\
            n{0,1}a{0,1}s{0,1}|\
            n{0,1}s{0,1}a{0,1}"

def fuzzyfy(type, length):

    fuzzystr = str("")

    #check type and length parameters for validity
    try:
        val = int(length)
    except:
        return None

    if type == '' or type == "":
        return None

    elif length < 1:
        return None

    match = re.fullmatch(regexstr, type)

    if not match:
        return None

    #build fuzzy string
    for i in range(0,length):
        fuzzystr += str(typeToChar(random.choice(type)))

    #check fuzzy string for expected legth
    if len(fuzzystr) == length:
        return fuzzystr
    else:
        return None

def typeToChar(type):
    #returns character for a given type
    if type == "a":
        return(random.choice(string.ascii_lowercase.join(string.ascii_uppercase)))
    elif type == "n":
        return(random.choice(string.digits))
    elif type == "s":
        return(random.choice(string.punctuation))
    else:
        return str("")

def test(runtest=False):
    if runtest:
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
test()
