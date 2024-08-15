# # # Exercícios
# # # 1 - Imprima a frase: Python na Escola de Programação da Alura.
# # print('Python na Escola de Programação da Alura.')
# # 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
# nome = input('Informe o seu nome:')
# idade = input('Informe a sua idade:')
# print(f'O seu nome é {nome} e você tem {idade} anos.')
# # 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
# # A
# # L
# # U
# # R
# # A
# print("""
#       A
#       L
#       U
#       R
#       A
#       """)

# # 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
# # pi = 3.14159

# pi = 3.14159
# pi_arredondado = round(pi, 2)
# print(f"O valor arredondado de pi é: {pi_arredondado}")
###########################################################################
# # 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
# numero = int(input('Informe um número:\n'))
# if numero % 2 == 0:
#     print(f'O número {numero} é par!')
# else:
#     print(f'O número {numero} é impar!')
# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# # Criança: 0 a 12 anos;
# # Adolescente: 13 a 18 anos;
# # Adulto: acima de 18 anos.
# idade = int(input('Informe a sua idade:\n'))
# if idade <= 12:
#     print('Você é uma criança')
# elif idade >= 13 and idade < 18:
#     print('Você é um adolescente')
# else:
#     print('Você é um adulto')


# # 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
# usuario_autorizado = "admin"
# senha_autorizada = "admin"
# usuario = input('Informe um nome de usuário:\n')
# senha = input('Informe a senha:\n')
# if usuario == usuario_autorizado and senha == senha_autorizada:
#     print('Acesso autorizado!')
# else:
#     print('Acesso negado!')

# # 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# # Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# # Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# # Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# # Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# # Caso contrário: o ponto está localizado no eixo ou origem.

# x = int(input('Informe a coordenada X:\n'))
# y = int(input('Infomre a coordenada Y:\n'))
# if x > 0 and y > 0:
#     print('Você está no PRIMEIRO QUADRANTE!')
# elif x < 0 and y > 0:
#     print('Você está no SEGUNDO QUADRANTE!')
# elif x < 0 and y < 0:
#     print('Você está no TERCEIRO QUADRANTE!')
# elif x > 0 and y < 0:
#     print('Você está no QUARTO QUADRANTE!')
# else:
#     print('Você está no EIXO ou ORIGEM!')
# # 1 - Crie uma lista para cada informação a seguir:

# # Lista de números de 1 a 10;
# # Lista com quatro nomes;
# # Lista com o ano que você nasceu e o ano atual.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nomes = ["Igor", "Gláucia", "João", "Théo"]
# anos = [1993, 2024]

# # 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for numero in numeros:
#     print(f'Numero {numero}')

# # 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# soma_impar = 0
# for impares in numeros:
#     if impares % 2 != 0:
#         soma_impar = soma_impar + impares
# print(soma_impar)

# # 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# for i in range(10, 0, -1):
#     print(i)

# # 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
# print("Bem vindo ao gerador de tabuada")
# numero = int(input("Informe o número desejado\n"))

# for i in range(1, 11, 1):
#     print(f"{numero} x {i} = {numero * i}")


# # 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
# try:
#     numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     soma = 0
#     for i in numeros:
#         soma += i
#     print(f"A soma de todos os elementos da lista é {soma}")
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')

# # 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
# try:
#     numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     media = 0
#     for numero in numeros:
#         media += numero
#     media = media / len(numeros)
#     print(f'A media dos elementos é de {media}')
# except numeros.length:
#     print("Erro")

# # Outra soluçao
# try:
#     numeros = [1,2,3,4,5,6,7,8,9,10]
#     if len(numeros) == 0:
#         raise ValueError("A lista está vazia, não é possível calcular a média.")
#     media = sum(numeros) / len(numeros)
#     print(f"A média dos valores da lista é de {media}")
# except ZeroDivisionError:
#     print("Erro: Impossível dividir por zero.")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")


# # 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
# dados_pessoal = [{"Nome": "Igor", "Idade": 30, "Cidade": "Recife"}]

# for dados in dados_pessoal:
#     nome = dados['Nome']
#     print(f'Nome {nome}')
# # 2 - Utilizando o dicionário criado no item 1:

# # Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# # Adicione um campo de profissão para essa pessoa;
# # Remova um item do dicionário.
# dados_pessoal = {"Nome": "Igor", "Idade": 30, "Cidade": "Recife"}


# nome = dados_pessoal['Nome']
# idade = dados_pessoal['Idade']
# cidade = dados_pessoal['Cidade']
# print(f'Nome {nome}, possui {idade} anos e reside em {cidade}')

# dados_pessoal['Idade'] = 31


# nome = dados_pessoal['Nome']
# idade = dados_pessoal['Idade']
# cidade = dados_pessoal['Cidade']
# print(f'Nome {nome}, possui {idade} anos e reside em {cidade}')

# dados_pessoal.update(Profissao = 'Dev')


# nome = dados_pessoal['Nome']
# idade = dados_pessoal['Idade']
# cidade = dados_pessoal['Cidade']
# profissao = dados_pessoal['Profissao']
# print(f'Nome {nome}, possui {idade} anos, reside em {cidade} e trabalha de {profissao}')

# del dados_pessoal['Profissao']


# nome = dados_pessoal['Nome']
# idade = dados_pessoal['Idade']
# cidade = dados_pessoal['Cidade']
# print(f'Nome {nome}, possui {idade} anos e reside em {cidade}.')

# # 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
# numeros_ao_quadrado = {}
# for numero in range(1, 6):
#     numeros_ao_quadrado[numero] = numero ** 2
# print(numeros_ao_quadrado)
# # 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
# dados_pessoal = {"Nome": "Igor", "Idade": 30, "Cidade": "Recife"}

# if 'Nome' in dados_pessoal:
#     print('A chave "Nome" existe no dicionario')
# else:
#     print('A chave "Nome" não existe no dicionario')

# # 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
# frase = "Olha que isso aqui ta muito bom isso aqui ta bom demais"
# frequencia_palavras = {}
# palavras = frase.split()

# for palavra in palavras:
#     if palavra in frequencia_palavras:
#         frequencia_palavras[palavra] += 1
#     else:
#         frequencia_palavras[palavra] = 1
# print(frequencia_palavras)
