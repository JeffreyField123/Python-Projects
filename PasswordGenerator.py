import random

print('This is a random password generator')

chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?$#%&')

number = input('How many passwords do you want to generate?: ')
number = int(number)


length = input('How many characters do you want your password(s) to be?: ')
length = int(length)

print('\nThese are your generated passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
