import string

def refine_words(center_letter:str) -> list[str]:
    # initialization and prep of all words that include the center letter
    file = open('SpellingBee/words_alpha.txt')
    words = file.readlines()
    refined_words = []
    for word in words:
        word = word.strip().lower()
        if center_letter in word and len(word) > 3:
            refined_words.append(word)
    file.close()

    return refined_words

def playable_words(refined_words:list[str], anti_letters:list[str]) -> list[str]:
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

    # sorting words by size then printing
    good_words = sorted(good_words, key=len)
    for word in good_words:
        print(f'{word} is a valid word')

    return good_words

def pangrams(good_words:list[str], target_letters:list[str]):
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


if __name__ == "__main__":
    center_letter = 'r'
    target_letters = ['c','g','i','m','n','p','r']
    anti_letters = list(string.ascii_lowercase)

    # creating anti letters list
    for letter in target_letters:
        anti_letters.remove(letter)

    refined = refine_words(center_letter=center_letter)
    playable = playable_words(refined_words=refined, anti_letters=anti_letters)
    pangrams(good_words=playable, target_letters=target_letters)
