str1 = "ls"
arr = []
for i in str1:
#对字符先转换为ASCII码，再转换为八进制
    lett = oct(ord(i))
    #这个主要是为了将八进制前面的0o替换掉
    lett=str(lett).replace("0o","")
    arr.append(lett)
sym = "\\"
# print(arr)
#将所有的八进制组合，最终的结果第一个地方应该再添加一个\
ccc=sym.join(arr)
print(ccc)


#最后将结果以这种形式输出即可绕过：$(printf "结果")