number = 35
if number > 100:
    print("A szám nagyobb, mint 100.")
else:
    print("A szám nem nagyobb, mint 100.")

if number % 2 == 0:
    print("A szám páros")
else:
    print("A szám nem páros")

number1 = 36
number2 = 9
if number1 % number2 == 0:
    print("Az egyik szám osztható a másikkal")
else:
    if number2 % number1 == 0:
        print("A másik szám osztható az elsővel.")
    else:
        print("A számok nem oszthatóak.")

if number1 % number2 == 0:
    print("Az egyik szám osztható a másikkal")
elif number2 % number1 == 0:
    print("A másik szám osztható az elsővel.")
else:
    print("A számok nem oszthatóak.")

radar = "radar2"
if radar[0] == radar[-1]:
    print("Az első és utolsó betű megegyezik")
else:
    print("Az első és utolsó betű nem egyezik meg.")

a = -1
if a > 0:
    print("a szám pozitiv")
elif a < 0:
    print("a szám negativ")
else:
    print("a szám nulla")

a = 3
b = 4
c = 2

if a >= b:
    if b >= c:
        print(a, b, c)
    elif a >= c:
        print(a, c, b)
    else:
        print(c, a, b)
