# coding=utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from flask import Flask
import support_library
from flask import Flask, render_template, request, make_response
#import nltk 
import langid
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hello():
    name=request.form['inputtext']
    #connect to the microsoft cloud for searching the various corpora of the english language with their corrosponding hindi corpora.
    #tokens = tokens = nltk.word_tokenize(name)
    #print tokens
    #pos_tagging = nltk.pos_tag(tokens)
    #print pos_tagging
    client = support_library.MicrosoftTranslatorClient('machinetranslationmanishrana','mjbYdQ3SyROItdT1gJAXUcIxYlBDaEKs3oKZ8XcFq0w=')
    language = langid.classify(name)
    print "printing language........."
    print language[0]
    if language[0] == 'en':    
        translated = client.TranslateText(name, 'en', 'hi')
        input_detected = "English"
        output_detected = "Hindi"
    else:
        translated = client.TranslateText(name, 'hi', 'en')
        input_detected = "Hindi"
        output_detected = "English"
    translated = translated.replace('"',"")
    print "translated is"
    print translated
    return render_template('index.html', name=name, translated=translated, input_detected=input_detected,output_detected=output_detected)


if __name__ == '__main__':
    app.run(debug=True) #this ensures auto reloading of the server on detecting any change in the backend.