str1 = 'разработка'
str2 = 'администрирование'
str3 = 'protocol'
str4 = 'standard'
bytes1 = str1.encode('utf-8')
bytes2 = str2.encode('utf-8')
bytes3 = str3.encode('utf-8')
bytes4 = str4.encode('utf-8')
str1 = bytes1.decode('utf-8')
str2 = bytes2.decode('utf-8')
str3 = bytes3.decode('utf-8')
str4 = bytes4.decode('utf-8')
print(str1)
print(str2)
print(str3)
print(str4)

