import pandas as pd


class Entrevistador():

    def __init__(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.resposta1 = resposta1
        self.resposta2 = resposta2
        self.resposta3 = resposta3
        self.resposta4 = resposta4
        self.resposta5 = resposta5
        self.data_hora_cadastro = data_hora_cadastro

    def desejaParticipar(self):
        aceite = input('Você aceita participar dessa pesquisa? ')
        if aceite.upper() == 'SIM':
            return True
        elif aceite.upper == 'NÃO':
            return False

    def dadosBasicos(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        # return self.dadosBasicos

    def set_pergunta1(self, resposta1):
        if resposta1 == 1:
            self.resposta1 = "Sim"
            return self.resposta1
        elif resposta1 == 2:
            self.resposta1 = "Não"
            return self.resposta1
        elif resposta1 == 3:
            self.resposta1 = "Não sei responder"
            return self.resposta1

    def set_pergunta2(self):
        return  # resposta 2: Sim, Não, Não Sei

    def set_pergunta3(self, resposta3):
        if resposta3 == 1:
            self.resposta3 = "Sim"
            return self.resposta3
        elif resposta3 == 2:
            self.resposta3 = "Não"
            return self.resposta3
        elif resposta3 == 3:
            self.resposta3 = "Não sei responder"
            return self.resposta3

    def set_pergunta4(self):
        return  # resposta 4: Sim, Não, Não Sei

    # recebe um valor entre 1 e 3 e devolve "Sim", "Não" ou "Não Sei".
    def set_pergunta5(self, resposta5):
        if resposta5 == 1:
            self.resposta5 = "Sim"
            return self.resposta5
        elif resposta5 == 2:
            self.resposta5 = "Não Sei"
            return self.resposta5
        elif resposta5 == 3:
            self.resposta5 = "Não"
            return self.resposta5

    def reunirRespostas(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5):
        resposta = {nome: [idade, sexo, resposta1,
                           resposta2, resposta3, resposta4, resposta5]}
        return resposta

    def pyToCSV(self, respostas):
        return  # arquivo csv

    def get_nome(self):
        return self.nome

    # atribui um novo nome caso o nome inserido já conste como key em um dicionário. Evita sobreposição de dados.
    def set_nomeRepetido(self, novoNome):
        self.nome = novoNome
        return self.nome

    # Data e hora:
    def horaeData(self, data_hora_cadastro):
        self.data_hora_cadastro = data_hora_cadastro
        return data_hora_cadastro

    def reunirRespostas(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro):
        resposta = {nome: [idade, sexo, resposta1, resposta2,
                           resposta3, resposta4, resposta5, data_hora_cadastro]}
        return resposta

    # Pessoal, acho que para gerar o dataframe o dicionario precisa estar nesse formado aqui em baixo, pois cada chave vira uma coluna
    # Deixei aqui em baixo comentado de sugestão para quando tiver a parte de gerar o csv a gente testar, tudo bem?

    # def reunirRespostas(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, data_hora_cadastro):
    #     resposta = {'Nome': nome,
    #                 'Idade': idade,
    #                 'Gênero': sexo,
    #                 'Resposta 1': resposta1,
    #                 'Resposta 2': resposta2,
    #                 'Resposta 3': resposta3,
    #                 'Resposta 4': resposta4,
    #                 'Data e hora': data_hora_cadastro}
    #     return resposta

    def pyToCSV(self, respostas):
        return  # arquivo csv
