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
    input5 = int(input(f'''Essa é uma pergunta teste. 
        1 - Sim
        2 - Não Sei
        3 - Não
        Digite a opção que melhor se aplica: '''))
    
    
    entrevistado = classe.Entrevistador(nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, input5)
    resposta5 = entrevistado.pergunta5(input5)

    resposta = entrevistado.reunirRespostas(nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5)
    respostas.update(resposta)

print(respostas)
