from flask import Flask
from flask import request
from spellcorrection import correct_misspelled_words
from keyword_extractor import rake_impl
from youtube_api import youtube_api_call

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/search')
def search():
    search_query = request.args['search_query']
    search_query = correct_misspelled_words(search_query)
    keywords = rake_impl(search_query)
    print(keywords)
    youtube_response = youtube_api_call(dict(keywords))
    return youtube_response

if __name__ == '__main__':
   app.run()
