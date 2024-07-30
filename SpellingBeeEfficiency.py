#time efficiency testing, same code copied and pasted 
import time
import string
from Spellingbee import refine_words, playable_words

# initialize everything
center_letter = 'o'
target_letters = ['a','k','l','o','t','u','w']
anti_letters = list(string.ascii_lowercase)
# creating anti letters list
for letter in target_letters:
    anti_letters.remove(letter)

#measuring time efficient algorithm speed
time_start = time.time()

r = refine_words('o')
playable_words(r, anti_letters=anti_letters)

time_end = time.time()

time_result = time_end - time_start

#measuring space efficient algorithm speed
space_start = time.time()

#space optimized refine words -> deleting off list instead of adding to a new one
file = open('words_alpha.txt')
words = file.readlines()
words = [w.strip().lower() for w in words]
for word in words:
    if center_letter not in word and len(word) < 3:
        words.remove(word)
file.close()

playable = True
for word in words:
    for letter in anti_letters:
        if letter in word:
            playable = False
            break
    if playable:
        words.remove(word)
    playable = True
words = sorted(words, key=len)

space_end = time.time()
space_result = space_end - space_start

print(f'The speed optimized algorithm ran in {time_result} seconds')
print(f'The space optimized algorithm ran in {space_result} seconds')
