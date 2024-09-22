import random
import string

def generate_password(length, difficulty):
    choices = {
        "easy": string.ascii_lowercase + string.digits,
        "medium": string.ascii_letters + string.digits,
        "hard": string.ascii_letters + string.digits + string.punctuation
    }
    
    characters = choices.get(difficulty, string.ascii_letters + string.digits)
    return ''.join(random.choice(characters) for _ in range(length))

# รับ input จากผู้ใช้
length = int(input("กรุณากำหนดความยาวของรหัสผ่าน: "))
difficulty = input("เลือกระดับความยาก (easy, medium, hard): ").lower()

# สุ่มรหัสผ่าน
password = generate_password(length, difficulty)
print(f"รหัสผ่านที่สุ่มได้คือ: {password}")
