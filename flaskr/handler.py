from flask import Flask
from flask import request
from flask import render_template
from flask_cors import CORS
from spellcorrection import correct_misspelled_words
from profanity_checker import profanity_check
from keyword_extractor import rake_impl
from youtube_api import youtube_api_call

app = Flask(__name__)
CORS(app)

@app.route('/')
def application_start():
    return "Hello"

@app.route('/search')
def search():
    search_query = request.args['search_query']
    search_query = correct_misspelled_words(search_query)
    if(profanity_check(search_query)):
        raise Exception("Foul language used")
    else:
        keywords = rake_impl(search_query)
        print(keywords)
        youtube_response = youtube_api_call(dict(keywords))
        return youtube_response

if __name__ == '__main__':
   app.run()
