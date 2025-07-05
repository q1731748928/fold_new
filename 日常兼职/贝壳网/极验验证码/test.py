hex_array = ["73", "27", "b7", "4b", "11", "2d", "95", "27", "82", "df", "1c", "77", "99", "05", "7a", "52", "cb", "d9", "f0", "5d", "e6", "21", "32", "f6", "e8", "7a", "49", "ca", "5b", "d1", "49", "4b", "6e", "e2", "80", "4f", "cf", "ff", "3f", "21", "e5", "55", "1e"]
# 将十六进制字符串转换为字节
byte_array = bytearray.fromhex(''.join(hex_array))
# 将字节数组转换为字符串
result_string = byte_array.decode('utf-8', errors='ignore')
print(result_string)