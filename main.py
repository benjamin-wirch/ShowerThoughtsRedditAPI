import requests
import keys

CLIENT_ID = keys.CLIENT_ID
SECRET_KEY = keys.SECRET_KEY
USERNAME = keys.USERNAME
PASSWORD = keys.PASSWORD
#Set this to desired subreddit (ex. news NOT r/news)
SUBREDDIT = 'showerthoughts'

headers = {'User-Agent': 'EducationalAPI/0.0.1'}
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD
}
req = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = req.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'

link = 'https://oauth.reddit.com/r/' + SUBREDDIT + '/top'
req = requests.get(link, headers=headers)

for post in req.json()['data']['children']:
    title = post['data']['title']
    print(title)

