from profanity_filter import ProfanityFilter
import spacy

def profanity_check(search_query):
    pf = ProfanityFilter(languages=['en'])
    pf.censor_whole_words = False
    search_query = pf.censor(search_query)
    print("censored")
    print(search_query)
    if "*" in search_query:
        return True
    else:
        return False
