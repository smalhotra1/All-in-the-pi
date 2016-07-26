from __future__ import print_function
import httplib2

import os
import datetime

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

#needed for opening browser
import webbrowser

#text to speech library
import pyttsx

engine = pyttsx.init()

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    print ("about to read events from the list")
    eve(Thread)
def eve( Thread):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    #url to calendar
    url = "https://calendar.google.com/calendar/embed?src=theraspberrianproject%40gmail.com&ctz=America/Chicago"

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    volume = engine.getProperty('volume')

    for voice in voices:
        engine.setProperty('volume', volume - 10.25)
        engine.setProperty('voice', voices[1].id)

        #engine.say("these are the events in calender")
    #engine.runAndWait()

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        time.sleep(2)

        print(start, event['summary'])
        engine.say(event['summary'])
        engine.runAndWait()
    #t = threading.Timer(4.0, event)
    #t.start()
    #webbrowser.open(url, new=0, autoraise=True)

if __name__ == '__main__':
    main()



