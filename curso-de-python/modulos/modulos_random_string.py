import random
import string

#escolher uma letra do alfabeto
print(random.choices(string.ascii_lowercase))
print(random.choices(string.ascii_uppercase))
print(random.choices(string.ascii_letters))