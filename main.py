import classe

aceite = bool
respostas = {} 

while classe.Entrevistador.desejaParticipar(aceite) == True:

    nome = input("Nome: ")
    idade = 19 
    sexo  = 'F' 
    resposta1 = 'a'
    resposta2 = 'b' 
    resposta3 = 'c' 
    resposta4 = 'd' 
    
    # A resposta da pergunta 5 é um numero entre 1 e 3 
    input5 = int(input(f'''Essa é uma pergunta teste.
    1 - Sim
    2 - Não Sei
    3 - Não
    Digite a opção que melhor se aplica: '''))
    
    # instanciamento do objeto entrevistado
    entrevistado = classe.Entrevistador(nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, input5)
    
    # o valor da resposta 5 deve ser "Sim", "Não" ou "Não Sei". Por isso, o método set_resposta5 traduz de número para palavra. 
    resposta5 = entrevistado.set_pergunta5(input5)

    # se inserirem nomes repetidos, os dados do item anterior com mesma key do dicionário serão substituídos. Por isso:
    if entrevistado.get_nome() in respostas:
        item = len(respostas)
        nomeNovo = entrevistado.get_nome() + " " + str(item)
        nome = entrevistado.set_nomeRepetido(nomeNovo)

    resposta = entrevistado.reunirRespostas(nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5)
    respostas.update(resposta)

print(respostas)
