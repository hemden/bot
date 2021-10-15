coding: 'utf-8'
from typing import Dict, Text, List, Optional, Any
import pandas as pd
import smtplib
import ssl
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict
from googletrans import Translator
translator= Translator()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# show projects
class ValidateRegisterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_rec_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        return []

    def validate_name(
        self,
        slot_value: Any,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
         return {"keyword": None}
        else: 
         return {"keyword": slot_value}	
class ActionSubmitcategorue(Action):
    def name(self) -> Text:
        return "action_submitcategorie"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        categorie= tracker.get_slot("categorie")
        print("your choice is : ",categorie) 
        dispatcher.utter_message(response="utter_categorie")
        return[]
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_keyword1"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        user_name = tracker.get_slot("keyword1")
        print("your choice is : ",user_name) 
        key=[]
        dispatcher.utter_message(response="utter_details_keyword1")
        return[]
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_keyword2"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        user_name = tracker.get_slot("keyword2")
        print("your choice is : ",user_name) 
        key=[]
        dispatcher.utter_message(response="utter_details_keyword2")
        return[]
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_keyword3"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        user_name = tracker.get_slot("keyword3")
        print("your choice is : ",user_name) 
        key=[]
        dispatcher.utter_message(response="utter_details_keyword3")
        return[]
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_keyword4"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        user_name = tracker.get_slot("keyword4")
        print("your choice is : ",user_name) 
        key=[]
        dispatcher.utter_message(response="utter_details_keyword4")
        return[]
class ActionSubmitkeyword2(Action):
    def name(self) -> Text:
        return "action_keyword5"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        keyword2 = tracker.get_slot("keyword5")
        print("your choice is : ",keyword2) 
        dispatcher.utter_message(response="utter_details_keyword5")
        return[]
class ActionSubmitkeyword2(Action):
    def name(self) -> Text:
        return "action_keyword6"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        keyword2 = tracker.get_slot("keyword6")
        print("your choice is : ",keyword2) 
        dispatcher.utter_message(response="utter_details_keyword6")
        return[]
class ActionSubmitkeyword2(Action):
    def name(self) -> Text:
        return "action_keyword7"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        keyword2 = tracker.get_slot("keyword7")
        print("your choice is : ",keyword2) 
        dispatcher.utter_message(response="utter_details_keyword7")
        return[]
class ActionSubmitkeyword2(Action):
    def name(self) -> Text:
        return "action_keyword8"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        keyword2 = tracker.get_slot("keyword8")
        print("your choice is : ",keyword2) 
        dispatcher.utter_message(response="utter_details_keyword8")
        return[]
class ActionSubmitkeyword2(Action):
    def name(self) -> Text:
        return "action_keyword9"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        keyword2 = tracker.get_slot("keyword9")
        print("your choice is : ",keyword2) 
        dispatcher.utter_message(response="utter_details_keyword9")
        return[]
class ActionSubmitkeyword2(Action):
    def name(self) -> Text:
        return "action_keyword10"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        keyword2 = tracker.get_slot("keyword10")
        print("your choice is : ",keyword2) 
        dispatcher.utter_message(response="utter_details_keyword10")
        return[]
class ActionSubmitkeyword2(Action):
    def name(self) -> Text:
        return "action_keyword11"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        keyword2 = tracker.get_slot("keyword11")
        print("your choice is : ",keyword2) 
        dispatcher.utter_message(response="utter_details_keyword11")
        return[]
class ActionSubmitkeyword2(Action):
    def name(self) -> Text:
        return "action_keyword12"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        keyword2 = tracker.get_slot("keyword12")
        print("your choice is : ",keyword2) 
        dispatcher.utter_message(response="utter_details_keyword12")
        return[]
class ValidateemailForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_email_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])->List[Dict[Text, Any]]:
        return []

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        """Validate slot value."""
        if not slot_value:
         return {"email": None}
        else: 
         return {"email": slot_value}	

class ActionSubmitemail(Action):
    def name(self) -> Text:
        return "action_submitemail"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        print("your choice is : ",email) 
        dispatcher.utter_message(response="utter_email")
        return[]
class Validatetopnform(FormValidationAction):
    def name(self) -> Text:
        return "validate_topn_form"
    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) ->  List[Dict[Text, Any]]:
        return []
    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        """Validate slot value."""
        if not slot_value:
         return {"topn": None}
        else :
            return {"topn": slot_value}	

class ActionSubmittopn(Action):
    def name(self) -> Text:
        return "action_submittopn"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        top = tracker.get_slot("topn")
        print("your choice is : ",top) 
        dispatcher.utter_message(response="utter_topn")
        return[]

class Action_recommand(Action):
    def name(self) -> Text:
        return "action_rec" 
    def run(self,dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        keywordlist=[]
        keyword=""
        keyword1= tracker.get_slot("keyword1") 
        keyword2= tracker.get_slot("keyword2") 
        keyword3= tracker.get_slot("keyword3") 
        keyword4= tracker.get_slot("keyword4") 
        keyword5= tracker.get_slot("keyword5") 
        keyword6= tracker.get_slot("keyword6") 
        keyword7= tracker.get_slot("keyword7") 
        keyword8= tracker.get_slot("keyword8") 
        keyword9 = tracker.get_slot("keyword9") 
        keyword10= tracker.get_slot("keyword10") 
        keyword11= tracker.get_slot("keyword11") 
        keyword12= tracker.get_slot("keyword12") 
        keywordlist.append(keyword1)
        keywordlist.append(keyword2)
        keywordlist.append(keyword3)
        keywordlist.append(keyword4)
        corpus=[]
       # for e in keywordlist:
        #    if e != "None":
                #keyword=keyword+" "+e
         #       corpus.append(e)
        if keyword1:
            print("here:",keyword1)
            keyword=  keyword+ keyword1 +" "
        if keyword2:
            print('2:',keyword2)
            keyword= keyword+ keyword2 +" "
        if keyword3:
            print('3:',keyword3)
            keyword=keyword+ keyword3 +" "
        if keyword4:
            print('4:',keyword4)
            keyword= keyword+ keyword4 +" "
        if keyword5:
            print('5:',keyword5)
            keyword= keyword+ keyword5 +" "
        if keyword6:
            print('6:',keyword6)
            keyword= keyword+ keyword6 +" "
        if keyword7:
            print('7:',keyword7)
            keyword= keyword+ keyword7 +" "
        if keyword8:
            print('8:',keyword8)
            keyword= keyword+ keyword8 +" "
        if keyword9:
            print('9:',keyword9)
            keyword= keyword+ keyword9 +" "
        if keyword10:
            print('10:',keyword10)
            keyword= keyword+ keyword10 +" "
        if keyword11:
            print('11:',keyword11)
            keyword= keyword+ keyword11 +" "
        if keyword12:
            print('12:',keyword12)
            keyword= keyword+ keyword12 +" "
         #keyword= keyword1 +" "+ keyword2+" "+ keyword3+" "+ keyword4
        #print("keyword:" ,keyword)
        
        
        topn=tracker.get_slot("topn")
        if (topn=="one"):
            top_n= 1 
        elif (topn=="two"):
            top_n= 2
        elif topn=="three":
            top_n= 3
        elif topn=="four":
            top_n=4
        elif topn=="five":
            top_n=5
        #if (keyword=='works'):
         #   keyword= "Travaux"
       # elif (keyword=='services'):
        #    keyword= "Fourniture de services"
        #elif (keyword== "Supply of goods"):
         #   keyword= "Fourniture de biens"
        #elif (keyword=="Studies"):
         #   keyword= 'Etudes'
        print("keyword: " ,keyword)
        print("top: ", top_n)
        base= pd.read_csv(r'C:\Users\asus\Desktop\internship\bot\ChatBot-Using-Rasa-2.0\base_recam.csv')
        corpus=list(base.text_final)
        corpus.append(keyword)
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(corpus)
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        sim_scores = list(enumerate(cosine_sim[len(corpus)-1]))
        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        top_n=top_n+1 
        sim_scores = sim_scores[1:top_n]
        annonce_indices = [i[0] for i in sim_scores]
        sims=[i[1] for i in sim_scores]
        indices=[i for i in annonce_indices]
        data=base[['id_annonce','Description','Categorie']].iloc[indices]
        data['Similarity']=sims
        data.index=list(indices)
        desc=[elem for elem in data.Description]   
        ids=[elem for elem in data.id_annonce]
        text=' '
        for i in range(len(desc)):
            x='We recommand for you this announce :\n id:{} {} \n ------------------- \n'.format(ids[i],desc[i])
            
            text+=x
        dispatcher.utter_message(text)
        

      
      
class Validatetypeform(FormValidationAction):
    def name(self) -> Text:
        return "validate_aucten_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        return []
    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        """Validate slot value."""
        if not slot_value:
         return {"aucten": None}
        else :
            return {"aucten": slot_value}	

class ActionSubmitaucten(Action):
    def name(self) -> Text:
        return "action_submitaucten"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        aucten = tracker.get_slot("aucten")
        print("your choice is : ",aucten) 
        dispatcher.utter_message(response="utter_aucten")
        return[]



class Validatelocationform(FormValidationAction):
    def name(self) -> Text:
        return "validate_location_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        return []
    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        """Validate slot value."""
        #states=["Tunis", "nabeul","zaghouane","sfax","ariana","beja","ben arous","bizerte","gabes","jendouba","kairouane","kasserine","kebili","kef","mahdia","mannouba","medenin","monastir","sidi bouzid","siliana","sousse","tataouin","tozeur"]
        if not slot_value:
         return {"location": None}
       # elif slot_value not in states:
         #   print("please enter a state ")
        else :
            return {"location": slot_value}	


class ActionSubmitlocation(Action):
    def name(self) -> Text:
        return "action_submitlocation"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        print("your choice is : ",location) 
        dispatcher.utter_message(response="utter_location")
        return[]


class searchAction(Action):

    def name(self) -> Text:
        return "action_search"
    def __init__(self):
        self.data = pd.read_csv('./actions/base_recam.csv') 
    def run(self,dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
     
        '''
        this function is destinated to the use of chatbot to facilitate the search for the user . It will return a specific list of announces depending to the user inputs  
        args: 
            lieux(str): Acheteur public/ Recette de douane
            types(str): either its Appel d'ofre or Ventes aux enchères
        output:
        result {DataFrame,text}: a dataframe(text) that contains all the announces depending the the user inputs
        '''
        
        types = tracker.get_slot("aucten")  
        Recipient= tracker.get_slot('email')
        #print("email:",Recipient)
        lieu = tracker.get_slot("location")
        print("type:",types)
        print("lieu:",lieu)
        lieux= self.data["Acheteur public/Recette douane"]
        column_values=[]
        ids=[]
        typ=""
        type= self.data["Type"]
        data=self.data
        if (types !="" and lieu != ""):
            for i in range(len(list(data))):
                if(types=="auction"):
                    typ="Vente aux enchères"
                elif(types== "call for tender"):
                    typ="Appel d'offre"
                #print(typ)
                if( typ.lower() == type[i].lower()  and lieu.lower() in lieux[i].lower()):
                    column_values.append(data["Description"][i]) 
                    ids.append(data["id_annonce"][i])       
            server = smtplib.SMTP_SSL('smtp.gmail.com',465) #connect to smtp server
            #server.starttls()
            sender= "hemdenrahma34@gmail.com"
            sender_pswd = "Semsem2021"
            server.login(sender, sender_pswd)  
            Subject= "search result"
            Body=""
            for j in range(len(column_values)):
                id = ids[j]
                cv= column_values[j]
                Body=  "id:"+id +" "+cv+"\n"   
            msg ="Subject: "+ Subject+ "\n\n" +Body 
            msg= msg.encode('utf8', 'replace')
            server.sendmail(sender, Recipient, msg)                         
            server.quit()  
            print('done')
            dispatcher.utter_message(" Email sent ! ")
            

        return()
class searchAction(Action):

    def name(self) -> Text:
        return "action_result"
    def __init__(self):
        self.data = pd.read_csv('./actions/base_recam.csv') 
    def run(self,dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
     
        '''
        this function is destinated to the use of chatbot to facilitate the search for the user . It will return a specific list of announces depending to the user inputs  
        args: 
            lieux(str): Acheteur public/ Recette de douane
            types(str): either its Appel d'ofre or Ventes aux enchères
        output:
        result {DataFrame,text}: a dataframe(text) that contains all the announces depending the the user inputs
        '''
        
        types = tracker.get_slot("aucten")  
        Recipient= tracker.get_slot('email')
        #print("email:",Recipient)
        lieu = tracker.get_slot("location")
        print("type:",types)
        print("lieu:",lieu)
        lieux= self.data["Acheteur public/Recette douane"]
        column_values=[]
        ids=[]
        typ=""
        type= self.data["Type"]
        data=self.data
        if (types !="" and lieu != ""):
            for i in range(len(list(data))):
                if(types=="auction"):
                    typ="Vente aux enchères"
                elif(types== "call for tender"):
                    typ="Appel d'offre"
                #print(typ)
                if( typ.lower() == type[i].lower()  and lieu.lower() in lieux[i].lower()):
                    column_values.append(data["Description"][i]) 
                    ids.append(data["id_annonce"][i])       
            

           
            Body=""
            for j in range(len(column_values)):
                id = ids[j]
                cv= column_values[j]
                Body=  "id:"+id +" "+cv+"\n"  
            dispatcher.utter_message("here is your result : \n")     
            dispatcher.utter_message(Body)
            

        return()


class cifexistAction(Action):

    def name(self) -> Text:
        return "action_cifexist"
    def __init__(self):
        self.data = pd.read_csv('./actions/base_recam.csv') 
    def run(self,dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
     
        '''
        this function is destinated to the use of chatbot to facilitate the search for the user . It will return a specific list of announces depending to the user inputs  
        args: 
            lieux(str): Acheteur public/ Recette de douane
            types(str): either its Appel d'ofre or Ventes aux enchères
        output:
        result {DataFrame,text}: a dataframe(text) that contains all the announces depending the the user inputs
        '''
        
        types = tracker.get_slot("aucten")  
        #Recipient= tracker.get_slot('email')
        #print("email:",Recipient)
        lieu = tracker.get_slot("location")
        print("type:",types)
        print("lieu:",lieu)
        lieux= self.data["Acheteur public/Recette douane"]
        column_values=[]
        ids=[]
        typ=""
        type= self.data["Type"]
        data=self.data
        if (types !="" and lieu != ""):
            for i in range(len(list(data))):
                if(types=="auction"):
                    typ="Vente aux enchères"
                elif(types== "call for tender"):
                    typ="Appel d'offre"
                #print(typ)
                if( typ.lower() == type[i].lower()  and lieu.lower() in lieux[i].lower()):
                    column_values.append(data["Description"][i]) 
                    ids.append(data["id_annonce"][i])       
            if(len(column_values)==0):
                   dispatcher.utter_message("there is no such offer  !")
                   dispatcher.utter_message(response="utter_again")
            else: 
                dispatcher.utter_message("searching.. plz wait ")
                dispatcher.utter_message(response="utter_mail"  )
                #dispatcher.utter_message(response="uttermail" )














import time

class UtterGreetings(Action):
    def name(self) -> Text:
        return "action_greetings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        curr_time = time.localtime().tm_hour
        if curr_time < 12: 
            dispatcher.utter_message(text = "good morning!")
        elif curr_time >= 12 and curr_time < 17:
            dispatcher.utter_message(text = "good afternoon!")
        else:
            dispatcher.utter_message(text = "good evening!")
        
        return []


class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_carousels"
    
    def run(self,dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Auction faq",
                        #"subtitle": "$10",
                        "image_url": "https://scontent.ftun16-1.fna.fbcdn.net/v/t1.15752-9/242121618_221030530075369_1176832921932214452_n.png?_nc_cat=105&ccb=1-5&_nc_sid=ae9488&_nc_ohc=EkSsKn03MKoAX806Plo&_nc_ht=scontent.ftun16-1.fna&oh=2054c43e14d9e5cab7394c1bea3d5f60&oe=616A752B",
                        "buttons": [ 
                            {
                            "title": "Tunisians Abroad",
                            "url": "https://www.douane.gov.tn/js-support-ticket-controlpanel/faqs/3/?pagenum=1",
                            "type": "web_url"
                           # "payload": "TunisiansAbroad",
                            #"type": "postback"
                            },
                            {
                            "title": "Direction Origin",
                            "url": "https://www.douane.gov.tn/js-support-ticket-controlpanel/faqs/2/",
                            "type": "web_url"
                           # "payload": "DirectionOrigin",
                            #"type": "postback"
                            },
                            {
                            "title": "Fiscal advantages",
                            "url" : "https://www.douane.gov.tn/js-support-ticket-controlpanel/faqs/1/",
                            "type": "web_url"
                            #"payload": "Fiscaladvantages",
                            #"type": "postback"
                            },
                            {
                            "title": "Economic Operators",
                            "url" : "https://www.douane.gov.tn/js-support-ticket-controlpanel/faqs/4/",
                            "type": "web_url"
                            #"payload": "EconomicOperators",
                            #"type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Call for tender faq ",
                        #"subtitle": "$12",
                        "image_url": "https://scontent.ftun16-1.fna.fbcdn.net/v/t1.15752-9/242153638_852164845689932_6726075691764555058_n.png?_nc_cat=100&ccb=1-5&_nc_sid=ae9488&_nc_ohc=kBVVuwi3XhUAX8cRVlt&_nc_ht=scontent.ftun16-1.fna&oh=2dbe741ccde7051a0b22be9c86ff8800&oe=61685C61",
                        "buttons": [ 
                            {
                            "title": "FAQ",
                            "url": "https://www.tuneps.tn/index.do",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message("i am made to help you get more information about auctions and tenders, may you choose !")
        dispatcher.utter_message( attachment=message)
        dispatcher.utter_message(response="utter_again")
        return []