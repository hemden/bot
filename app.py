import json
from flask import Flask, request, render_template, Response
import  requests
from flask_pymongo import PyMongo
from flask_cors import CORS,cross_origin
#from flask_socketio import SocketIO
from rasa.nlu.model import Interpreter
from textblob import TextBlob
import googletrans
from googletrans import Translator
#import speech_recognition as sr
#from langdetect import detect
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#from manager import Manager
#from gtts import gTTS
#import playsound
translator= Translator()
app = Flask(__name__,  template_folder='templates')
#app.config['MONGO_URI']= 'mongodb://localhost:27017/bot_conv'
#mongo= PyMongo(app)



#model_path=r"C:\Users\asus\Desktop\internship\rasa\saved_models\nlu"
@app.route('/bot', methods = ['POST', 'GET'])
@cross_origin()
def index():
    return render_template('index.html')
config_path=r"C:\Users\asus\Desktop\internship\rasa\config.json"
check_point=r"C:\Users\asus\Desktop\internship\rasa\integration\checkpoint\CHECKPOINT_NAME.tar"
#SocketIO(app,cors_allowed_origins="http://localhost:5005/")
@app.route('/',methods = ['POST','GET'])
@cross_origin()
def index_get():
    if request.method == 'GET':
        val = str(request.args.get('text'))
       # val= val.text
        #print("*********",request.args.get())
        #lang = TextBlob(val)
       # language = lang.detect_language()
        #print(language,"******************")
       # output= translator.translate(val,src=language,dest='en')
       # print(output)
       # val=output.text
        #val=val.txt
       # print("val:" ,val)
        data = json.dumps({"sender": "Rasa", "message": val})
        print(data)
       # mongo.db.record.insert(dict(data))
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        #nlu_interpreter = Interpreter.load(model_path)
        #intent = nlu_interpreter.parse(val)['intent']
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
        #confidence = intent['confidence']
        #if (confidence < 0.5):
         #   m1 = Manager(config_path, 'inference', check_point)
          #  val = m1.predict(val)
          #  val = val.json()
        #else:
         #   res = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
        res = res.json()
        val = res[0]['text']
        #outt= translator.translate(val,src='en',dest=language)
        #val = outt.text
       # val=val.txt
    return render_template('index.html', val=val)

if __name__ == '__main__':
    app.run(debug=True)