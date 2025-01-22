# hesap makinesi:

a = int(input("Lutfen ilk sayiyi giriniz:"))
b = int(input("Lutfen ikinci sayiyi giriniz:"))

c = input("Lutfen islem gir:")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
else:
    print("Yanlis bir deger girdin!")