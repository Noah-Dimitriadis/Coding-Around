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

def record_result(guessed_word:str, result:str):
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
    
def check_result(result:str) -> bool:
    for letter in result:
        if letter != 'g':
            return False
    return True

def get_result() -> str:
    while True:
        result = input('Enter the result from your guessed word: ')
        if len(result) == 5:
            return result
        
def refine_words(guessed_word:str, result:str, all_words:list[str]) -> list[str]:
    turn = dict()
    for i in range(5):
        turn.update({result[i]:guessed_word[i]})
    for word in all_words:
        for grey_letter in grey_letters:
            if grey_letter in word:
                del all_words[all_words.index(word)]
                print(f'removing {all_words[i]}')
                break
            
    return all_words
    
if __name__ == '__main__':
    huffman_pairs = load_letter_frequencies()
    # print(huffman_pairs)

    # all_words = load_words()
    # guessed_word = get_guessed_word().lower()
    # result = get_result().lower()
    # check_result(result)
    # record_result(guessed_word, result)
    # refined_words = refine_words(guessed_word, result, all_words)

    # for word in refined_words:
    #     if 'f' in word:
    #         print(word)

    for pair in huffman_pairs:
        print(f'{pair}:{huffman_pairs.get(pair)}')