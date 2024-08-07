

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
        huffman_pairs.update({pair[0]:pair[1]})
    
    return huffman_pairs
    

if __name__ == '__main__':
    huffman_pairs = load_letter_frequencies()
    print(huffman_pairs)