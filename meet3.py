bil_integer = 100
print (type(bil_integer))

print("tipe data dari bil_integer adalah",(type(bil_integer)))

bil_float = 2,5
print (type(bil_float))

print("tipe data dari bil_float adalah",(type(bil_float)))

bil_string = "hakki"
print (type(bil_string))

print("tipe data dari bil_string adalah",(type(bil_string)))

bil_bol = False
print (type(bil_bol))

print("tipe data dari bil_bol adalah",(type(bil_bol)))

from ctypes import c_double
bil_double = c_double(3000000000)
print(type(bil_double))