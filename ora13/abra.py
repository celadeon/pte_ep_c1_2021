from matplotlib.pyplot import *

number_of_points = 100
x, y1, y2, y3 = [], [], [], []
for i in range(number_of_points):
    x.append(i)
    y1.append(i)
    y2.append(i ** 2)
    y3.append(i ** 3)
plot(x, y1, "r", label="y = x")
plot(x, y2, "g", label="y = x2")
plot(x, y3, "b", label="y = x3")
axis([0, 10, 0, 30])
title("my diagram")
grid(True)
xlabel("x")
ylabel("y")
legend()
show()

