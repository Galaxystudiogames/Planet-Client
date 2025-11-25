import json
import minecraft_launcher_lib


#Azure Stuff
CLIENT_ID = "01cabc92-07d5-445d-9bde-0d43161fc331"
REDIRECT_URL = "http://localhost:8080"
login_url, state, code_verifier = minecraft_launcher_lib.microsoft_account.get_secure_login_data(CLIENT_ID,REDIRECT_URL)



def AddAccount(token):

    data = minecraft_launcher_lib.microsoft_account.complete_login(client_id= CLIENT_ID,
                                                                   client_secret= None,
                                                                   redirect_uri= REDIRECT_URL,
                                                                   auth_code= token,
                                                                   code_verifier= code_verifier,)
    print(data)
    with open("accounts.json",'w') as f:
        json.dump(data,f)