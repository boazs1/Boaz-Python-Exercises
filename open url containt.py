import urllib.request

fp = urllib.request.urlopen("http://www.ynet.co.il")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
#print(mystr)
result = mystr.find("boaz")
print(result);
