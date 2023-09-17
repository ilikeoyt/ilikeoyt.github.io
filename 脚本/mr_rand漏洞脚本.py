str1 ='czsnvXb9Lk'#随机数的一部分或者另外一个随机数
str2 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"#随机数的范围
result =''


length = str(len(str2)-1)
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if str1[i] ==  str2[j]:
            result += str(j) + ' ' +str(j) + ' ' + '0' + ' ' + length + ' '
            break


print(result)
#将结果放入linux中得到其他或者完整的随机数
#进入mt_seed，输入./php_mt_seed 结果
#得到种子

