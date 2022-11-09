from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", static_folder="static")

@app.route("/englishToFrench")
def englishToFrench(englishText):
    textToTranslate = request.args.get('textToTranslate')
    return translator.english_to_french(english_text=textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.french_to_english(french_text=textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template('mywebscript.js')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
