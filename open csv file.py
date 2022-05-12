import csv
import rook

import urllib.request

rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f',
    labels=None,
    git_commit='bfdd9510bfcbb7c9b990d10a9fb6d3356abad565',
    git_origin='https://github.com/boazs1/Boaz-Python-Exercises'
   )
i = 1


fp = urllib.request.urlopen("http://www.ynet.co.il")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
print(mystr)
while i < 25000:
    print(mystr)
    i += 1
