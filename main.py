import classe
from datetime import datetime

aceite = bool
respostas = {}

while classe.Entrevistador.desejaParticipar(aceite) == True:

    nome = input("Nome: ")
    idade = 19
    sexo = 'F'
    resposta1 = 'a'
    resposta2 = 'b'
    resposta3 = 'c'
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
    
    resposta1 = entrevistado.set_pergunta1(input1)
    resposta3 = entrevistado.set_pergunta3(input3)
    resposta5 = entrevistado.set_pergunta5(input5)
    data_hora_cadastro = entrevistado.horaeData(data_hora_cadastro)

    # se inserirem nomes repetidos, os dados do item anterior com mesma key do dicionário serão substituídos. Por isso:
    if entrevistado.get_nome() in respostas:
        item = len(respostas)
        nomeNovo = entrevistado.get_nome() + " " + str(item)
        nome = entrevistado.set_nomeRepetido(nomeNovo)

    
    resposta = entrevistado.reunirRespostas(
        nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro)
    respostas.update(resposta)

print(respostas)