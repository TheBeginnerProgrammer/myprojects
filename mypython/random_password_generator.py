#generate random password
import string
import random

letters = string.ascii_letters
numbers = string.digits
punctuations = "!@#$%^&8()"

password_length = int(input("Enter password length: "))


def password_generator(length=8):

    result = f'{letters}{numbers}{punctuations}'
    result = list(result)
    random.shuffle(result)
    random_password = random.choices(result,k=length)
    random_password =''.join(random_password)
    return random_password

print(password_generator(password_length))
    



