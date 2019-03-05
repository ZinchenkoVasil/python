str1 = "разработка"
str2 = "сокет"
str3 = "декоратор"
print(f"string: {str1}, type: {type(str1)}")
print(f"string: {str2}, type: {type(str2)}")
print(f"string: {str3}, type: {type(str3)}")
bytes1 = str1.encode('utf-8')
bytes2 = str2.encode('utf-8')
bytes3 = str3.encode('utf-8')
print(f"bytes: {bytes1}, type: {type(bytes1)}")
print(f"bytes: {bytes2}, type: {type(bytes2)}")
print(f"bytes: {bytes3}, type: {type(bytes3)}")

