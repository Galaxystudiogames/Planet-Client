import webbrowser
import minecraft_launcher_lib




#Azure Stuff
CLIENT_ID = "01cabc92-07d5-445d-9bde-0d43161fc331"
REDIRECT_URL = "http://localhost:8080"
login_url, state, code_verifier = minecraft_launcher_lib.microsoft_account.get_secure_login_data(CLIENT_ID,REDIRECT_URL)


def Login():
    # Login
    webbrowser.open_new(url=login_url)
    StartServer()



#Login()
