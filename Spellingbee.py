import string

center_letter = 'c'
target_letters = ['a','c','g','h','i','n','r']
all_letters = list(string.ascii_lowercase)

# creating anti letters list
anti_letters = []
for letter in all_letters:
    if letter not in target_letters:
        anti_letters.append(letter)

# initialization and prep of all words that include the center letter
refined_words = []
all_words = open('words_alpha.txt').readlines()
for word in all_words:
    word = word.strip().lower()
    if center_letter in word and len(word) > 3:
        refined_words.append(word)

# create list of all words that can be played
count = 0
good_words = []
for word in refined_words:
    for letter in anti_letters:
        if letter in word:
            count += 1
            break
    if count == 0:
        good_words.append(word)
        print(f'{word} is a valid word')
    count = 0
print()

# print all words that are pangrams and perfect pangrams
pangram = 0
for word in good_words:
    for letter in target_letters:
        if letter in word:
            pangram += 1
    if pangram >= 7:
        if len(word) == 7:
            print(f'{word} is a Perfect Pangram')
        else:
            print(f'{word} is a Pangram')
    pangram = 0