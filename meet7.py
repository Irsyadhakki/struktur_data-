# tabel kebenaran (Logika Bolean)
# and or not xor

# NOT
print("\n**********Logika NOT*************")
x = False
y = not x
print("nilai dari x =", x)
print("nilai dari y =", y)

# AND (hanya bernilai benar, ketika keduanya benar)
# akan bernilai salah, selama ada satu yang salah
print("\n**********Logika AND*************")
x = False
y = False
z = x and y
print(x, "and", y, "=", z)

x = False
y = True
z = x and y
print(x, "and", y, "=", z)

x = True
y = False
z = x and y
print(x, "and", y, "=", z)

x = True
y = True
z = x and y
print(x, "and", y, "=", z)

# OR (hanya bernilai benar, selama ada satu aja yang true)
# bernilai salah,, ketika keduanya salah
print("\n**********Logika OR*************")
x = False
y = False
z = x or y
print(x, "OR", y, "=", z)

x = False
y = True
z = x or y
print(x, "OR", y, "=", z)

x = True
y = False
z = x or y
print(x, "OR", y, "=", z)

x = True
y = True
z = x or y
print(x, "OR", y, "=", z)

# XOR
#
print("\n**********Logika XOR*************")

x = False
y = False
z = x ^ y
print(x, "XOR", y, "=", z)

x = False
y = True
z = x ^ y
print(x, "XOR", y, "=", z)

x = True
y = False
z = x ^ y
print(x, "XOR", y, "=", z)

x = True
y = True
z = x ^ y
print(x, "XOR", y, "=", z)