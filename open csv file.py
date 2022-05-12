import csv
import rook
import sentry_sdk
import urllib.request

 sentry_sdk.init(
    dsn="https://2acefaf842814814848afd40457bc55d@sentry.io/1381062",
    integrations=[FlaskIntegration()]
)
rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f',
    labels=None,
 
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
