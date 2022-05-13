import urllib.request

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

import rook
rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
