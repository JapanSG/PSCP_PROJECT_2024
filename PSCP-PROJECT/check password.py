"""check password"""
import re
def main() :
    """output"""
    password = str(input())
    result = check(password)
    print(result)
def check(password) :
    """check"""
    score = 0
    if len(password) >= 8 :
        score += 1
    if len(password) >= 12 :
        score += 1

    if re.search(r"[0-9]", password) :
        score += 1

    if re.search(r"[A-Z]", password) :
        score += 1

    if re.search(r"[a-z]", password) :
        score += 1

    if re.search(r"[!-/]", password) or re.search(r"[:-@]", password) or re.search(r"[[-`]", password) or re.search(r"[{-~]", password) :
        score += 1

    # if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) or re.search(r"[']", password) or:
    #     score += 1

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
main()

# import re
# b = "#"
# a = bool(re.search(r"!@#$%^&*()_+|~-=\`{}[]:";'<>?,./",b))
# print(a)

