import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
model_id = 'en-fr'
model_id2 = 'fr-en'
englishText = 'This is python programming'
frenchText = 'Il s agit d une programmation Python'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

translation = language_translator.translate(
    text=englishText,
    model_id=model_id).get_result()
#print(json.dumps(translation, indent=2, ensure_ascii=False))

def englishToFrench(englishText):
    frenchText = translation
    return frenchText


translation2 = language_translator.translate(
    text=frenchText,
    model_id=model_id2).get_result()


def frenchToEnglish(frenchText):
    englishText = translation2
    return englishText

translatedText = englishToFrench(englishText)
translatedText2 = frenchToEnglish(frenchText)

print(translatedText)
print(translatedText2)