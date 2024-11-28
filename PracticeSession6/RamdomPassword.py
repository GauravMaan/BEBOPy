import random
import string


def generate_password(length):
    if length < 4:
        return "Password length must be at least 4"
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)
password=generate_password(int(input("enter the number: ")))
print(password)