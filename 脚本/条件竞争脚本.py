import requests
url="http://192.168.0.104:8080/upload-labs-master/upload/1.php"
while True:
	web_result=requests.get(url)
	if web_result.status_code == 200:
		print("Success")
		break
	else:
		print("Failed")
