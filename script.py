import requests
import json,urllib

#Configuration

#1)set your access token
access_token="Enter your access token here"

#2)Bulk activation(True) or bulk deactivation(False)
bulk_activation=True

#3)Specify the input file with list of usernames separated by '\n'
fo = open("input.txt", "r")

for uname in fo:
    get_url="https://www.facebook.com/scim/v1/Users?filter=userName+eq%22"+uname.rstrip()+"%22&access_token="+access_token.rstrip()
    r=requests.get(get_url)
    d = json.loads(r.text)
    try:
        uid=d["Resources"][0]["id"]
    except IndexError:
        print(uname.rstrip()+": Does not exist in workplace")
    else:
        put_url="https://www.facebook.com/scim/v1/Users/"+str(uid)+"?access_token="+access_token.rstrip()
        r=requests.get(put_url)
        d=json.loads(r.text)
        if bulk_activation:
		d["active"]=True
	else:
		d["active"]=False
        payload = json.dumps(d)
        r1 = requests.put(put_url, data=payload)
        print(uname.rstrip()+": Activation successfull")
