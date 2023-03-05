import getdata
import time

#Formats data into 16x2 char format for 1602 LCD screen
while True:
    lists = getdata.makelist()
    splitwords = []

    for s in lists:
        words = s.split()
        temp = ''
        for w in words:
            if len(temp + w) <= 16:
                temp += w + ' '
            else:
                splitwords.append(temp[:-1])
                temp = w + ' '
        splitwords.append(temp[:-1])
        splitwords.append('\n')
        splitter = ''
    for i in range(0, len(splitwords), 2):
        grouper = splitwords[i: i+2]
        if len(grouper) < 2:
            print(grouper[0])
            time.sleep(4)
            continue
        else:
            print(grouper[0])
            print(grouper[1])
            time.sleep(4)
