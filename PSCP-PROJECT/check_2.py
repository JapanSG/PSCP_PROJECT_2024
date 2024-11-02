"""checkpassword"""
def check():
    """Password"""
    password = str(input())
    score = 0
    countlower = 0
    countupper = 0
    countnum = 0
    countsymbol = 0
    symbols = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','|',\
            '\\',':',';','\"','\'','<',',','>','.','?','/'}

    if len(password) >= 8 :
        score += 1
    if len(password) >= 12 :
        score += 1

    for i in password:
        if i.islower():
            countlower += 1
        if i.isupper():
            countupper += 1
        if i.isnumeric():
            countnum += 1
        if i in symbols:
            countsymbol += 1
    if countlower:
        score += 1
    if countnum:
        score += 1
    if countupper:
        score += 1
    if countsymbol:
        score += 1

    if score <= 1 :
        return "very weak"
    if score == 2 :
        return "weak"
    if score == 3 :
        return "good"
    if 4 <= score <= 5 :
        return "strong"
    if score >= 6 :
        return "very strong"
print(check())
