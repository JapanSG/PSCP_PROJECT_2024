import random
import string

def generate_password(length, difficulty):
    if difficulty == "easy":
        characters = string.ascii_lowercase + string.digits
    elif difficulty == "medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

# input 
length = int(input("Lenght of Password: "))
difficulty = input("Difficult of Password (easy, medium, hard): ").lower()

# random 
print("Password :", generate_password(length, difficulty))
