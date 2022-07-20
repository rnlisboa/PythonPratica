import random 
valores = list()
for i in range(100):
    x = random.randint(1,1000)
    if x not in valores:
        valores.append(x)
#print(valores)
valores.sort()
#valores.sort(reverse = true) coloca os valores em ordem decrescente
print(len(valores))