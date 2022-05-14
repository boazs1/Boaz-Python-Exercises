import urllib.request
import rook
from flask import Flask, render_template
app = Flask(__name__)
rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f')

fp = urllib.request.urlopen("http://www.ynet.co.il")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
i = 1
while i < 1000000:
    print(mystr)
    i = i + 1

#result = mystr.find("boaz")
#print(result);
