for i in range(128,65537):
    tmp = chr(i)
    try:
        res = tmp.encode('idna').decode('utf-8')
        if("-") in res: #出现-说明不符合要求，直接排除
            continue
        if "c" in res:
            print("ascii:{}  tmp:{}  res:{}".format(i,tmp,res))
    except:
        pass