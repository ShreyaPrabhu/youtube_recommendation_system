import RAKE
import operator

def rake_impl(search_query):
    stop_dir = "stoplist.txt"
    rake_object = RAKE.Rake(stop_dir)
    keywords = rake_object.run(search_query)
    print ("keywords: ", keywords)
    return keywords
