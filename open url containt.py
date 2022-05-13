import urllib.request

fp = urllib.request.urlopen("http://www.ynet.co.il")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
i = 1
while i < 1000000:
    print(mystr)
    i = i + 1
