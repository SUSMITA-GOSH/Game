import random
import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)


def generate_password(length):
    value = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(value) for _ in range(length))
    return password

pass_len = 10

while True:
    password = generate_password(pass_len)
    print("Your password is:", password)
    
    user_response = input("Do you like this password? (yes/no): ").strip().lower()
    if user_response == 'yes':
        print("Password accepted.")
        break
    elif user_response == 'no':
        print("Generating a new password...")
    else:
        print("Invalid response. Please type 'yes' or 'no'.")
