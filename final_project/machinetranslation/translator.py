"""Module providing e2f f2e translators."""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishtofrench(inputenglishtext):
    frenchdict = language_translator.translate(text=inputenglishtext,model_id='en-fr').get_result()
    outputfrenchtext = frenchdict['translations'][0]['translation']
    return outputfrenchtext

def frenchtoenglish(inputfrenchtext):
    englishdict = language_translator.translate(text=inputfrenchtext,model_id='fr-en').get_result()
    outputenglishtext = englishdict['translations'][0]['translation']    
    return outputenglishtext

