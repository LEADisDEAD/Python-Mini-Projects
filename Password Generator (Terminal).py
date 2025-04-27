# Password gen (terminal)
import random
import string

lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
specials = list(string.punctuation)
digits = list(string.digits)
def PasswordGenerator():

    password = []
    password += random.choices(digits,k=3)
    password += random.choices(lower_letters,k=3)
    password += random.choices(upper_letters,k=3)
    password += random.choices(specials,k=3)

    random.shuffle(password)
    passw = "".join(password)
    return passw

def PassGenUser(cus_num,cus_lc,cus_uc,cus_sp):
    password = []
    password += random.choices(digits, k=cus_num)
    password += random.choices(lower_letters, k=cus_lc)
    password += random.choices(upper_letters, k=cus_uc)
    password += random.choices(specials, k=cus_sp)

    random.shuffle(password)
    passw = "".join(password)
    return passw


print("---Password Generator---")

user_choice = input("Auto generated or custom password? (gen/cus) :").lower().strip()

if(user_choice == "gen"):
    passw = PasswordGenerator()
    print(f"Your password: {passw}")
elif(user_choice == "cus"):
    cus_num = int(input("Enter number of digits: "))
    cus_lc = int(input("Enter number of lowercase characters: "))
    cus_uc = int(input("Enter number of uppercase characters: "))
    cus_sp = int(input("Enter number of special characters: "))

    passw = PassGenUser(cus_num,cus_lc,cus_uc,cus_sp)
    print(f"Your password: {passw}")
else:
    print("Invalid input")

