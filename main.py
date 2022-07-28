import classe
from datetime import datetime

respostas = []
idade = ''
condicao = True

while condicao:
    print('----------')

    idade = input('Digite sua idade (para finalizar o programa, digite 00): ')

    if idade == '00':
        condicao = False

    if condicao == True:
        nome = input("Digite seu nome: ")
        sexo = int(input(
            'Digite o número relacionado ao gênero no qual você se identifica:\n [1] - Feminino\n [2] - Masculino\n [3] - Não binário: '))
        sexo = classe.Entrevistado.validaResposta(classe.Entrevistado, sexo)

        print('----------')

        input1 = (input(
            '---------- \n Pergunta 1: Você tem acesso à internet banda larga em casa?\n [1] - Sim\n [2] - Não\n [3] - Não sei responder\n Digite a opção que melhor se aplica: '))
        input1 = classe.Entrevistado.validaResposta(
            classe.Entrevistado, input1)

        input2 = int(input(
            '---------- \n Pergunta 2: Você utiliza computador ou notebook em casa para acesso à internet?\n [1] - Sim\n [2] - Não\n [3] - Não sei responder\n Digite a opção que melhor se aplica: '))
        input2 = classe.Entrevistado.validaResposta(
            classe.Entrevistado, input2)

        input3 = int(input(
            '---------- \n Pergunta 3: Você utiliza celular (ou tablet) para acesso à internet?\n [1] - Sim\n [2] - Não\n [3] - Não sei responder\n Digite a opção que melhor se aplica: '))
        input3 = classe.Entrevistado.validaResposta(
            classe.Entrevistado, input3)

        input4 = int(input(
            '---------- \n Pergunta 4: Você precisa da internet para fins educacionais? (aula/curso)\n [1] - Sim\n [2] - Não\n [3] - Não sei responder\n Digite a opção que melhor se aplica: '))
        input4 = classe.Entrevistado.validaResposta(
            classe.Entrevistado, input4)

        input5 = int(input(
            '---------- \n Pergunta 5: A conexão da sua internet é estável? (não desconecta com frequencia)\n [1] - Sim\n [2] - Não\n [3] - Não sei responder\n Digite a opção que melhor se aplica: '))
        input5 = classe.Entrevistado.validaResposta(
            classe.Entrevistado, input5)

        data_hora_cadastro = datetime.now()

        # instanciamento do objeto entrevistado
        entrevistado = classe.Entrevistado(nome, idade, data_hora_cadastro)

        # atribui os valores fornecidos (1, 2 ou 3) à variável resposta como Sim, Não e Não sei responder, respectivamente.
        resposta1 = entrevistado.pergunta(input1)
        resposta2 = entrevistado.pergunta(input2)
        resposta3 = entrevistado.pergunta(input3)
        resposta4 = entrevistado.pergunta(input4)
        resposta5 = entrevistado.pergunta(input5)

        idade = classe.Entrevistado.validaIdade(classe.Entrevistado, idade)

        # atribuir o valor (1,2 ou 3) à variável resposta como Feminino, Masculino e Não Binário, respectivamente.
        sexo = entrevistado.dadosSexo(sexo)

        # cria um dicionário para cada entrevistado
        resposta = entrevistado.reunirRespostas(
            nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro)

        # cria a lista de respostas com os dicionários dos entrevistados
        respostas.append(resposta)

    else:
        print('Pesquisa finalizada! Obrigada por participar!')
        # criar um dataframe e, em seguida, criar o arquivo .csv
        entrevistado.pyToCsv(respostas)
