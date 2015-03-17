from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file,client,tools
CLIENT_SECRET='/Users/gudaprudhvihemanth/Desktop/client_secret.json'
SCOPES='https://www.googleapis.com/auth/webmasters.readonly'
store=file.Storage('storage.json')
credz=store.get()
if not credz or credz.invalid:
    flow=client.flow_from_clientsecrets(CLIENT_SECRET,SCOPES)
    credz=tools.run(flow,store)
SERVICE = build('webmasters','v3', http=credz.authorize(Http()))
site_list = SERVICE.sites().list().execute()
print site_list