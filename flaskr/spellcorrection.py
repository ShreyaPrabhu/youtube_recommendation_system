from spellchecker import SpellChecker
import string

def correct_misspelled_words(search_query):
    all_words = search_query.translate(str.maketrans('', '', string.punctuation)).split()
    spell = SpellChecker()
    misspelled = spell.unknown(all_words)
    for wrong_word in misspelled:
        # Get the one `most likely` answer
        correct_word = spell.correction(wrong_word)
        print(wrong_word)
        print(correct_word)
        search_query = search_query.replace(wrong_word, correct_word)
    print(search_query)
    return search_query
