import random
from math import sqrt
import emoji
num = random.randint(1,100)
raiz = sqrt(num)
print('\n',num)
#print(f'\n {raiz:.2f}')
print(emoji.emojize(f"Olá {raiz:.2f} :sunglasses:", language='alias'))