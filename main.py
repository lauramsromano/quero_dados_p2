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

    entrevistado = classe.Entrevistador(
        nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, input5, data_hora_cadastro)
    resposta1 = entrevistado.pergunta1(input1)
    resposta3 = entrevistado.pergunta3(input3)
    resposta5 = entrevistado.pergunta5(input5)
    data_hora_cadastro = entrevistado.horaeData(data_hora_cadastro)

    resposta = entrevistado.reunirRespostas(
        nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro)
    respostas.update(resposta)

print(respostas)
