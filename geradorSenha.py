import random
tamanho = int(input('Informe o tamanho da senha: '))
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*'
limite = len(caracteres) - 1
senha = ''
for i in range(tamanho):
    index = random.randint(0, limite)
    senha += caracteres[index]
print('Sua senha gerada é: ', senha)