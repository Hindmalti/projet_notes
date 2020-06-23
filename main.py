import requests
import os

LOGIN_URL= "https://portail.polytech-lille.fr/login/"
GET_NOTES_URL = "http://appliportal.polytech-lille.fr/mypolytech/mesNotes.php"
URI = "aHR0cHM6Ly9wb3J0YWlsLnBvbHl0ZWNoLWxpbGxlLmZy"

#Première etape : Log In pour récupérer le cookie
with requests.Session() as session:

    payload = {
        'login': os.environ['LOGIN'],
        'password': os.environ['PASSWORD'],
        'uri': URI
    }

    files = []
    
    headers= {}

    response = session.request("POST", LOGIN_URL, headers=headers, data = payload, files = files)

    print(session.cookies.get_dict())


#Seconde étape : Utiliser le cookie

    response = session.request('GET', url=GET_NOTES_URL, headers=headers, payload={})
    parse_notes(response.raw)

#Troisième étape : Parser la réponse HTML => Récupérer toutes les notes

def parse_notes(html_file):



#Quatrième étape : Comparer NOTRE liste des notes à la liste sur DynamoDB