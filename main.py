import sys

login = "admin"
s_password = "password123"

def check_login(username, password):
    if username == login and password == s_password:
        return True
    else:
        return False

username = input("Логинді енгізіңіз: ")
password = input("Пароліңізді енгізіңіз: ")

if check_login(username, password):
    print("Доступ берілді")
    sys.exit(0)
else:
    print("Қате")
    sys.exit(1)
