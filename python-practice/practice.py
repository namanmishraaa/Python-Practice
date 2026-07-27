a = "10"
b = 5
print(int(a) + b)
print(100*'*')
x = "3.14"
y = 2
print(float(x) + y)
print(100*'*')
print(bool("False"))  #True
print(bool(""))   #False
print(bool(0))  #False
print(bool("0")) #True
print(100*'*')
s = "Hello, World!"

reversed_s = s[::-1]
lower_s = s.lower()
starts_with_hello = s.startswith("Hello")
  # hint: strings have a method for this
print(100*'*')
name = "Nammo"
score = 95.6789
print(f"{name} scored {score:.2f} points")