import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    desired_length = int(input("Enter desired password length: "))
    if desired_length <= 0:
        print("Invalid length. Please enter a positive integer.")
    else:
        generated_password = generate_password(desired_length)
        print(f"Your new password: {generated_password}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")