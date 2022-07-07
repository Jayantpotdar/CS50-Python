from string import ascii_letters,digits,punctuation
from itertools import product

for passcode in product(ascii_letters+digits+punctuation, repeat=3):
    print(*passcode)