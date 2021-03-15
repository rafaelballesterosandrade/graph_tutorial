# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# <FirstCodeSnippet>
from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  user = graph_client.get('{0}/me'.format(graph_url))
  # Return the JSON result
  return user.json()
# </FirstCodeSnippet>

# <GetCalendarSnippet>
def get_calendar_events(token):
  graph_client = OAuth2Session(token=token)

  # Configure query parameters to
  # modify the results
  query_params = {
    '$select': 'subject,organizer,start,end',
    '$orderby': 'createdDateTime DESC'
  }

  # Send GET to /me/events
  events = graph_client.get('{0}/me/events'.format(graph_url), params=query_params)
  # Return the JSON result
  return events.json()
# </GetCalendarSnippet>

def get_user_list(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  #users = graph_client.get('{0}/users'.format(graph_url))
  url_temp = '{0}/users?$count=true&$search="displayName:Rafael"&$filter=endsWith(mail,'+"'usalesiana.edu.bo')&$orderBy=displayName&$select=id,displayName,mail"
  print('//////////////////////////////////////////////////////////////')
  print(url_temp)
  users = graph_client.get(url_temp.format(graph_url))

  # Return the JSON result
  return users.json()

def get_user_dato(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  users = graph_client.get('{0}/me'.format(graph_url))
  # Return the JSON result
  return users.json()

