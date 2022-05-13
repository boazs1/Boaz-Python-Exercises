import urllib.request
import rook


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

if __name__== "__main__":
    rook.start()
    app.run(host="0.0.0.0", port=5000, threaded=True)
