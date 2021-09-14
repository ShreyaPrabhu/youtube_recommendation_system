# Youtube Recommendation Application

A flask based python application that interprets user search query using RAKE, performs spell check and profanity check and returns a list of youtube video recommendations.

![Demo video](demo16mb.mov)
Click on this link and select view raw. The demo video should get downloaded in local.

### Backend -
Flask framework
Python
RAKE library for keyword extraction
spellchecker library to correct spellings in search query
profanity_filter library for profanity check

### Frontend -
Materializecss and Javascript

### Getting Youtube API Key
- Head over to Google cloud console and create a project
- Select credentials and generate an API Key (Do not share or make it public)
- Copy this key and replace it in youtube_api.py file

### How to run this application
- Install all packages of correct version based on the list in pipfile
- Move into flaskr folder and execute ```python3 handler.py```
- Backend should now be running in your localhost at port 5000
- Move into frontend folder and open the html file in browser
- Play around!

More details on various NLP libraries that were tried out can be found here -
https://github.com/ShreyaPrabhu/keyword_extraction
