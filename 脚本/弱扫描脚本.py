import requests
url = 'http://da8dbfaf-2f76-487c-85a8-6826747544d9.node4.buuoj.cn:81/'

arr = ('flag.php','use.php','robots.txt','index.php','index.phps','flag.txt','var/log/ngnix/access.log','var/log/ngnix/error.log','.bak','index.php.git','index.php.hg','.git/head','admin','www.zip','index.php.rar','login.php','config.php','index.phps','secret.php','var/www/html','class.php','file.php','function.php','check.php','index.php.swp','index.php.bak','phpmyadmin','www.tar.gz', 'fAke_f1agggg.php','secrettw.php','doLogin.php','download.php','change.php','search.php','confirm.php','image.php','user.php','dir.php','query.php','secret','uploads','upload','register.php')
i = 0
while i <= len(arr) :
    res = url + arr[i]
    response = requests.get(url=res)
    if response.status_code == 200:
        print(res)
    i = i + 1