import requests
from typing import Generator

from ShowerThoughtsRedditAPI import keys


__all__ = (
    'getdata',
    'DEFAULT_SUBREDDIT',
)

DEFAULT_SUBREDDIT = 'showerthoughts'
HeaderGenerator = Generator[dict, None, None]
DataGenerator = Generator[str, None, None]


def __headers__(CLIENT_ID: str = keys.CLIENT_ID,
                SECRET_KEY: str = keys.SECRET_KEY,
                USERNAME: str = keys.USERNAME,
                PASSWORD: str = keys.PASSWORD) -> HeaderGenerator:
    '''Generate required auth information'''
    headers = {'User-Agent': 'EducationalAPI/0.0.1', }

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    data = {
        'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD,
    }

    with requests.post('https://www.reddit.com/api/v1/access_token',
                       auth=auth, data=data, headers=headers) as response:
        TOKEN = response.json()['access_token']

    headers['Authorization'] = f'bearer {TOKEN}'

    while True:
        yield headers


def getdata(subreddit: str = DEFAULT_SUBREDDIT,
            headers: HeaderGenerator = __headers__()) -> DataGenerator:
    subreddit = subreddit.strip('/')
    if '/' in subreddit:
        if not subreddit.startswith('r/'):
            raise ValueError(f'{subreddit} is not a valid subreddit.')
        subreddit = subreddit[2:]

    url = f'https://oauth.reddit.com/r/{subreddit}/top'

    with requests.get(url, headers=next(headers)) as response:
        assert response.ok, f'{url} returned a status_code={response.status_code}'

        return (
            post['data']['title'] for post in response.json()['data']['children']
        )


# ensure keys are never used again
del keys
del HeaderGenerator
del DataGenerator

if __name__ == '__main__':
    import sys

    subreddit = DEFAULT_SUBREDDIT

    if len(sys.argv) > 1:
        subreddit = sys.argv[1]

    *map(print, getdata(subreddit))
