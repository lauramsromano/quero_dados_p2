
import classe
from datetime import datetime

respostas = []
idade = ''
condicao = True

while condicao:
    print('----------')

    idade = input('Digite sua idade: ')
    if idade == '00':
        condicao = False

    if condicao == True:
        nome = input("Digite seu nome: ")
        sexo = int(input(
            'Digite o número relacionado ao gênero no qual você se identifica:\n [1] Feminino\n [2] Masculino\n [3] Não binário\n'))

        print('----------')

        input1 = int(input(f'''Essa é uma pergunta teste. 
        1 - Sim
        2 - Não 
        3 - Não sei responder
        Digite a opção que melhor se aplica: '''))
        

        input2 = int(input('''
        Você acha que empresas como a Resilia, focadas no ensino da tecnologia e empregabilidade, ajudam a 
        diminuir a Exclusão Digital no Brasil? 

        [1] Sim
        [2] Não
        [3] Não sei dizer
        Digite a opção que melhor se aplica:   '''))

        input3 = int(input(f'''Essa é uma pergunta teste. 
        1 - Sim
        2 - Não 
        3 - Não sei responder
        Digite a opção que melhor se aplica: '''))

        input4 = int(input('''
        Você acha que negros e pardos têm menos acesso à internet e à inclusão digital no Brasil? 

        [1] Sim
        [2] Não
        [3] Não sei dizer
        Digite a opção que melhor se aplica:   '''))

        input5 = int(input(f'''Essa é uma pergunta teste. 
        1 - Sim
        2 - Não Sei
        3 - Não
        Digite a opção que melhor se aplica: '''))

        data_hora_cadastro = datetime.now()

        # instanciamento do objeto entrevistado
        entrevistado = classe.Entrevistador(nome, idade, data_hora_cadastro)

        # atribui os valores fornecidos (1, 2 ou 3) à variável resposta como Sim, Não e Não sei responder, respectivamente.
        resposta1 = entrevistado.pergunta1(input1)
        resposta2 = 'b'
        resposta3 = entrevistado.pergunta3(input3)
        resposta4 = 'a'
        resposta5 = entrevistado.pergunta5(input5)

        # atribuir o valor (1,2 ou 3) à variável resposta como Feminino, Masculino e Não binário, respectivamente.
        sexo = entrevistado.dadosSexo(sexo)

        # cria um dicionário para cada entrevistado
        resposta = entrevistado.reunirRespostas(
            nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro)

        # cria a lista de respostas com os dicionários dos entrevistados
        respostas.append(resposta)

    else:
        print('Pesquisa finalizada! Obrigada por participar!')
        entrevistado.pyToCsv(respostas)

print(respostas)
