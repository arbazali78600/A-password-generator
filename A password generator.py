import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
  
    password = ''.join(random.choices(characters, k=length))
    
    return password


try:
    length = int(input("Enter desired password length: "))
    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")