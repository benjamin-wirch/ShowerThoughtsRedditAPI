import time

from ShowerThoughtsRedditAPI import getdata, DEFAULT_SUBREDDIT

# Formats data into 16x2 char format for 1602 LCD screen
while True:
    # data is now a generator
    data = getdata(DEFAULT_SUBREDDIT)
    splitwords = []

    for s in data:
        words = s.split()
        temp = ''
        for w in words:
            if len(f'{temp}{w}') <= 16:
                temp = f'{temp}{w} '
                continue

            splitwords.append(temp.strip())
            temp = f'{w} '
        splitwords.append(f'{temp.strip()}\n')

    for i in range(0, len(splitwords), 2):
        grouper = splitwords[i: i + 2]
        print(*grouper, sep='\n')
        time.sleep(4)
