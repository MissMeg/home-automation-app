from __future__ import print_function
# specific calendar id
from keys import cal_key
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Gcalendar:
    def __init__(self):
        self.events = []

    def gcal_connect(self):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 2 events on the user's calendar.
        """

        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        events_result = service.events().list(calendarId=cal_key, timeMin=now,
                                            maxResults=2, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            return 'No upcoming events found.'
        return self.set_data(events)

    def set_data(self, events):
        for event in events:
            self.events.append(
                dict(
                    summary=event['summary'],
                    start=event['start'].get('dateTime', event['start'].get('date')),
                    location=event['location'] if 'location' in event.keys() else ''
                )
            )
        return tuple(self.events)


if __name__ == '__main__':
    cal = Gcalendar()
    print(cal.gcal_connect())
