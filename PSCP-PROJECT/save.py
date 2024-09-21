'''save'''
def add_password(username : str, password : str) -> None:
    '''Add username and password to a file'''
    with open("password.txt","a") as file:
        file.write(f"username: {username}\n")
        file.write(f"password: {password}\n")
def clear_file() -> None:
    '''Clear all content in a file'''
    open("password.txt","w").close()
def main():
    '''Driver Code'''
    username = input()
    password = input()
    add_password(username,password)
if __name__ == "__main__":
    clear_file()
