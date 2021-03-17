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
  print('////////////////// LISTA ////////////////////////////////////////////')
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

def get_user_new(token):
  new_user = {
    'accountEnabled': true,
    'city': 'Seattle',
    'country': 'United States',
    'department': 'Sales & Marketing',
    'displayName': 'Melissa Darrow',
    'givenName': 'Melissa',
    'jobTitle': 'Marketing Director',
    'mailNickname': 'MelissaD',
    'passwordPolicies': 'DisablePasswordExpiration',
    'passwordProfile': {
        'password': 'fe472207-f759-b923-99d8-87cd01bba1d1',
        'forceChangePasswordNextSignIn': false
    },
    'officeLocation': '131/1105',
    'postalCode': '98052',
    'preferredLanguage': 'en-US',
    'state': 'WA',
    'streetAddress': '9256 Towne Center Dr., Suite 400',
    'surname': 'Darrow',
    'mobilePhone': '+1 206 555 0110',
    'usageLocation': 'US',
    'userPrincipalName': 'MelissaD@usalesiana.edu.bo'
  }

  # Set headers
  headers = {
    'Authorization': 'Bearer {0}'.format(token),
    'Content-Type': 'application/json'
  }

  requests.post('{0}/me/events'.format(graph_url),
    headers=headers,
    data=json.dumps(new_user))
    




  