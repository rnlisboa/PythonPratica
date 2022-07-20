import random
turma = list()
for i in range(100):
    nome = 'Aluno_ ' + str(i).zfill(3)
    etapa_1 = random.randint(0,100)
    etapa_2 = random.randint(0,100)
    media = (etapa_1* 2 + etapa_2 * 3) / 5
    turma.append([nome, etapa_1, etapa_2,media])
#turma.sort(key = lambda coluna: coluna[3]) ordena pela terceira coluna(media)    
turma.sort(key = lambda coluna: coluna[3])
print(turma)