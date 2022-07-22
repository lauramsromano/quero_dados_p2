from ast import Break
import classe
from datetime import datetime

respostas = []
idade = int

while True: #tem que corrigir esse while
    idade = int(input('Digite sua idade: '))
    
    if idade != 00:
        nome = str(input("Digite seu nome: "))
        sexo = int(input(
                'Digite o número relacionado ao gênero no qual você se identifica: [1] Feminino\n [2] Não binário\n [3] Masculino\n'))

        input2 = 'b'
        input4 = 'd'

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
            nome, idade, sexo, input1, input2, input3, input4, input5, data_hora_cadastro)

        # atribui os valores fornecidos (1, 2 ou 3) à variável resposta como Sim, Não ou Não Sei.
        resposta1 = entrevistado.set_pergunta1(input1)
        resposta2 = 'b'
        resposta3 = entrevistado.set_pergunta3(input3)
        resposta4 = 'a'
        resposta5 = entrevistado.set_pergunta5(input5)

        # inclui a hora em que o cadastro da resposta foi feito.
        data_hora_cadastro = entrevistado.horaeData(data_hora_cadastro)

        # cria um dicionário para cada entrevistado
        resposta = entrevistado.reunirRespostas(nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro)
        
        # cria a lista de respostas
        respostas.append(resposta)
    
    else:
        
        break

print(respostas)
