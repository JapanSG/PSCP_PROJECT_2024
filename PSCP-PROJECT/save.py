'''save'''
def add_password(username : str, password : str) -> None:
    '''Add username and password to a file'''
    with open("password.txt","a") as file:
        file.write(f"username: {username}\n")
        file.write(f"password: {password}\n")
def clear_file() -> None:
    '''Clear all content in a file'''
    open("password.txt","w").close()
def read_file() -> None:
    '''Read all content in a file'''
    with open("password.txt","r") as file:
        lines = file.read()
        return lines
        # num = 1
        # for i in range(0,len(lines),2):
        #     print(num)
        #     print(lines[i],lines[i+1],sep = "")
        #     num += 1
def get_pass(line_num:int)->str:
    '''Return username and password at a specific line'''
    with open("password.txt","r") as file:
        lines = file.readlines()
        line_num = line_num*2-2
        return f"{lines[line_num]}{lines[line_num+1]}"
def main():
    '''Driver Code'''
    username = input()
    password = input()
    add_password(username,password)
    read_file()
if __name__ == "__main__":
    main()
