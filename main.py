from ast import Break
import classe
from datetime import datetime

aceite = bool
respostas = {}
# Pelo que verifiquei para conseguir gerar o dataframe dá mais certo se juntar os dict em uma lista.
# Deixei aqui em baixo comentado de sugestão para quando tiver a parte de gerar o csv a gente testar, tudo bem?
# respostas = []

while classe.Entrevistador.desejaParticipar(aceite) == True:

    nome = str(input("Digite seu nome: "))  # não é necesário
    idade = int(input('Digite sua idade: '))
    if idade > 00:
        sexo = int(input(
            'Digite o número relacionado ao gênero no qual você se identifica: [1] Feminino\n [2] Não binário\n [3] Masculino\n'))

    elif idade == 00:  # mover para o final
        print('Fim do questionário')
        Break

    sexo = 'F'
    resposta2 = 'b'
    resposta4 = 'd'

    input1 = int(input(f'''Essa é uma pergunta teste. 
    1 - Sim
    2 - Não 
    3 - Não sei responder
    Digite a opção que melhor se aplica: '''))

    input3 = int(input(f'''Essa é uma pergunta teste. 
    1 - Sim
    2 - Não 
    3 - Não sei responder
    Digite a opção que melhor se aplica: '''))

    input5 = int(input(f'''Essa é uma pergunta teste. 
        1 - Sim
        2 - Não Sei
        3 - Não
        Digite a opção que melhor se aplica: '''))

    data_hora_cadastro = datetime.now()

    # instanciamento do objeto entrevistado
    entrevistado = classe.Entrevistador(
        nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, input5, data_hora_cadastro)

    # atribui os valores fornecidos (1, 2 ou 3) à variável resposta como Sim, Não ou Não Sei.
    resposta1 = entrevistado.set_pergunta1(input1)
    resposta3 = entrevistado.set_pergunta3(input3)
    resposta5 = entrevistado.set_pergunta5(input5)

    # inclui a hora em que o cadastro da resposta foi feito.
    data_hora_cadastro = entrevistado.horaeData(data_hora_cadastro)

    # se inserirem nomes repetidos, os dados do item anterior com mesma key do dicionário serão substituídos. Por isso:
    if entrevistado.get_nome() in respostas:
        item = len(respostas)
        nomeNovo = entrevistado.get_nome() + " " + str(item)
        nome = entrevistado.set_nomeRepetido(nomeNovo)

    # utiliza o método para reunir as respostas como entrada em um dicionário.
    resposta = entrevistado.reunirRespostas(
        nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro)
    respostas.update(resposta)

print(respostas)
