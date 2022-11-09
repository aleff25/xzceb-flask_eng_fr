"""Translate file to easy use"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(version="2018-05-01", authenticator=authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    """Translate the text from French to english"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def french_to_english(french_text):
    """Translate the text from english to French"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation']