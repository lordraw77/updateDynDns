import requests
import os
import json

env_variables = os.environ
#print(os.environ)
DYNDNS_USERNAME=env_variables['DYNDNS_USERNAME']
DYNDNS_PASSWORD=env_variables['DYNDNS_PASSWORD']
DYNDNS_HOST=env_variables['DYNDNS_HOST']

def updatednydns():
    url = f"https://update.dyndns.it/nic/update?hostname={DYNDNS_HOST}&username={DYNDNS_USERNAME}&password={DYNDNS_PASSWORD}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Response:')
            tresponse = response.text
            print(tresponse) 
            sendtelegram(f"update dnydns {tresponse}")
        else:
            print(f"Error response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erorr: {e}")


def sendtelegram(text):
    try:
        DYNDNS_SENDTELEGRAM=env_variables['DYNDNS_SENDTELEGRAM']
    except:
        DYNDNS_SENDTELEGRAM=False
     
    if bool(DYNDNS_SENDTELEGRAM)==True:
        print("1")
        DYNDNS_BOTKEY=env_variables['DYNDNS_BOTKEY']
        DYNDNS_CHATID=env_variables['DYNDNS_CHATID']
        print(DYNDNS_BOTKEY)
        print(DYNDNS_CHATID)
        body =  {}
        botkey = DYNDNS_BOTKEY
        chat = DYNDNS_CHATID
        
        url = f"https://api.telegram.org/{botkey}/sendMessage"

        headers = {
                'Content-Type': 'application/json'
            }

        body["chat_id"]=chat
        body["text"]=text
        response = requests.request("POST", url, headers=headers, data=json.dumps(body))
        text1 = response.text
        print(text1)


if __name__ == "__main__":
   updatednydns()
