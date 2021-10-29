python = "pythonban prgogramozunk"
print("a python szo 1. karaktere", python[0])
print("a python szo utolso karaktere", python[5])
print("a python szo utolso karaktere", python[-1])
print("a python szo utolso karaktere", python[len(python) - 1])

print("python valtozo 5-szor egymas utan", python * 5)

str2 = "hallgato"
str3 = "hiaba a hegyne anyag, a hallgato gyorsan halad"
print(str2 in str3)
print(python in str3)
print(python not in str3)

print(str3[0:5])
print(str3[0:3])

print(python + str2 + str3)
print(python, str2, str3, sep=" alma ")

str4 = "HALLGATO"
print(str4 in str3)
print(str4 in str2)
print(str4 > str2)