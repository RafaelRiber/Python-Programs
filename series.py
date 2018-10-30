import matplotlib.pyplot as plt

somme= 0
n = 100
a = 1
r = 0.5
i = 0

x=list()
y=list()

for i in range(1, n):
    somme = somme+ (a * (r ** (i-1)))
    i = i + 1
    x.append(i)
    y.append(somme)

print x
print y
plt.scatter(x, y)
plt.show()
