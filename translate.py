import googletrans
from textblob import TextBlob
#from spacy_langdetect import LanguageDetector
#import spacy
import pandas as pd
#from langdetect import detect
from googletrans import Translator
translator= Translator()
#text ="how are you ? "
#text ="كيف الحال"
#language= detect(text)
#text2="how is that possible"
#print(language)
#out= translator.translate(text2,src='en',dest=language)
#print(out.text)
#d1=translator.detect(text)
#print(d1['lang'])
#print(googletrans.LANGUAGES)
#print(out.text)
#nlp = spacy.load('en')  # 1
#nlp.add_pipe(LanguageDetector(), name='language_detector', last=True) #2
#text_content = "Er lebt mit seinen Eltern und seiner Schwester in Berlin."
#doc = nlp(text_content) #3
#detect_language = doc._.language #4
#print(detect_language)



#lang = TextBlob(text)
#language=lang.detect_language()
#print(language)
#types="call for tender"
#output= translator.translate(text,src=language,dest='fr')
#text =output.text

#print(text)
 

#df_es = pd.read_csv(r'C:\Users\asus\Downloads\inmigrantes_curso_español_2021.csv',sep=';',encoding='latin-1')
#df_en = df_es.copy()
#df_en.rename(columns=lambda x: translator.translate(x).text, inplace=True)
#print(df_en.columns)


df = pd.DataFrame({'Spanish':['piso','cama']})
df['English'] = df['Spanish'].apply(translator.translate, src='es', dest='en').apply(getattr, args=('text',))
print(df)