text = input("请输入需要转换的字符串：")

result = ""

for char in text:
    if char.isalpha():
        hex_str = hex(ord(char))[2:]  # 将10进制转换为16进制，并去掉前缀0x
        result += "%" + hex_str
    else:
        result += char

print("转换后的结果为：", result)