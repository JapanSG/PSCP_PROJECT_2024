import random
import string
import time

# ฟังก์ชันสร้างรหัสผ่าน
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# เริ่มจับเวลา
start_time = time.time()

# กำหนดความยาวของรหัสผ่านที่ต้องการ
password_length = 12

# เรียกใช้ฟังก์ชันสร้างรหัสผ่าน
password = generate_password(password_length)

# หยุดจับเวลา
end_time = time.time()

# แสดงรหัสผ่านและเวลาที่ใช้ในการสร้าง
print(f"Generated Password: {password}")
print(f"Time taken: {end_time - start_time:.10f} seconds")
