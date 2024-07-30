import string

center_letter = 'o'
target_letters = ['a','k','l','o','t','u','w']
anti_letters = list(string.ascii_lowercase)

# creating anti letters list
for letter in target_letters:
    anti_letters.remove(letter)

# initialization and prep of all words that include the center letter
file = open('words_alpha.txt')
words = file.readlines()
refined_words = []
for word in words:
    word = word.strip().lower()
    if center_letter in word and len(word) > 3:
        refined_words.append(word)
file.close()

# create list of all words that can be played
playable = True
good_words = []
for word in refined_words:
    for letter in anti_letters:
        if letter in word:
            playable = False
            break
    if playable:
        good_words.append(word)
    playable = True

good_words = sorted(good_words, key=len)
for word in good_words:
    print(f'{word} is a valid word')

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