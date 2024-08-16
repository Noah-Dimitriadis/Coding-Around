import string

guessed_words = []
green_letters = []
yellow_leters = []
grey_letters = []

def load_words() -> list[str]:
    file = open('Wordle/5LetterWords.txt')
    words = file.readlines()
    file.close()
    return [w.strip() for w in words]

def load_letter_frequencies() -> dict:
    file = open('Wordle/LetterFrequencies.txt')
    lines = file.readlines()
    file.close()
    
    huffman_pairs = dict()
    for pairs in lines:
        pair = pairs.strip().split(',')
        huffman_pairs.update({pair[0]:float(pair[1])})
    return huffman_pairs  

def check_letters(guessed_word:str, result:str):
    guessed_word = guessed_word.lower()
    result = result.lower()
    combined = dict()    
    for i in range(len(guessed_word)):
        combined.update({guessed_word[i]:result[i]})

    for key, value in combined.items():
        if value == 'g':
            print(f'{key} is a green letter')
            green_letters.append(key)
        elif value == 'y':
            yellow_leters.append(key)
            print(f'{key} is a yellow letter')
        else:
            grey_letters.append(key)
            print(f'{key} is a grey letter')
    
def get_guessed_word() -> str:
    while True:
            guessed_word = input('Enter the guessed word: ')
            if guessed_word not in guessed_words and len(guessed_word) == 5:
                guessed_words.append(guessed_word)
                return guessed_word
        
def get_result() -> str:
    while True:
        result = input('Enter the result from your guessed word: ')
        if len(result) == 5:
            return result
        
def get_valid_words(all_words:list[str]) -> list[str]:
    valid_words = all_words
    for word in all_words:
        for letter in word:
            if letter in grey_letters:
                valid_words.remove(word)
                break
            elif letter not in yellow_leters or letter not in green_letters:
                if word not in valid_words:
                    break
                valid_words.remove(word)
                break
        
    return valid_words

if __name__ == '__main__':
    # huffman_pairs = load_letter_frequencies()
    # print(huffman_pairs)
    all_words = load_words()
    # for i in range (6):
    guessed_word = get_guessed_word()
        # print(i)
    result = get_result()
    check_letters(guessed_word, result)
    valid_words = get_valid_words(all_words)
    print(len(valid_words))
    print(valid_words)
        
    