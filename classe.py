import pandas as pd


class Entrevistador():

    # atributos inicias da classe
    def __init__(self, nome, idade, data_hora_cadastro):
        self.nome = nome
        self.idade = idade
        self.data_hora_cadastro = data_hora_cadastro

    # receber um valor entre 1 e 3 e devolver "Feminino", "Masculino" ou "Não Binário"
    def dadosSexo(self, sexo):
        if sexo == 1:
            self.sexo = "Feminino"
            return self.sexo
        elif sexo == 2:
            self.sexo = "Masculino"
            return self.sexo
        elif sexo == 3:
            self.sexo = "Não Binário"
            return self.sexo

    # recebe um valor entre 1 e 3 e devolver "Sim", "Não" ou "Não sei responder".
    def pergunta1(self, resposta1):
        if resposta1 == 1:
            self.resposta1 = "Sim"
            return self.resposta1
        elif resposta1 == 2:
            self.resposta1 = "Não"
            return self.resposta1
        elif resposta1 == 3:
            self.resposta1 = "Não sei responder"
            return self.resposta1

    # recebe um valor entre 1 e 3 e devolver "Sim", "Não" ou "Não sei responder".
    def pergunta2(self, resposta2):
        if resposta2 == 1:
            self.resposta2 = "Sim"
            return self.resposta2
        elif resposta2 == 2:
            self.resposta2 = "Não"
            return self.resposta2
        elif resposta2 == 3:
            self.resposta2 = "Não sei responder"
            return self.resposta2

    # recebe um valor entre 1 e 3 e devolver "Sim", "Não" ou "Não sei responder".
    def pergunta3(self, resposta3):
        if resposta3 == 1:
            self.resposta3 = "Sim"
            return self.resposta3
        elif resposta3 == 2:
            self.resposta3 = "Não"
            return self.resposta3
        elif resposta3 == 3:
            self.resposta3 = "Não sei responder"
            return self.resposta3

    # recebe um valor entre 1 e 3 e devolver "Sim", "Não" ou "Não sei responder".
    def pergunta4(self, resposta4):
        if resposta4 == 1:
            self.resposta4 = "Sim"
            return self.resposta4
        elif resposta4 == 2:
            self.resposta4 = "Não"
            return self.resposta4
        elif resposta4 == 3:
            self.resposta4 = "Não sei responder"
            return self.resposta4

    # recebe um valor entre 1 e 3 e devolver "Sim", "Não" ou "Não sei responder".
    def pergunta5(self, resposta5):
        if resposta5 == 1:
            self.resposta5 = "Sim"
            return self.resposta5
        elif resposta5 == 2:
            self.resposta5 = "Não Sei"
            return self.resposta5
        elif resposta5 == 3:
            self.resposta5 = "Não"
            return self.resposta5

    # acessar o nome de um entrevistado
    def get_nome(self):
        return self.nome

    # reuniar as respostas do entrevistado e criar um dicionário
    def reunirRespostas(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro):
        resposta = {'Nome': nome,
                    'Idade': idade,
                    'Gênero': sexo,
                    'Resposta_1': resposta1,
                    'Resposta_2': resposta2,
                    'Resposta_3': resposta3,
                    'Resposta_4': resposta4,
                    'Resposta_5': resposta5,
                    'Data_e_hora': data_hora_cadastro}
        return resposta

    # verificar se já existe um arquivo .csv
    def verificarCsv(self):
        try:
            arquivo = pd.read_csv('resultados.csv')
            return arquivo
        # caso não tenha o arquivo, criar um dataframe e, em seguida, criar o arquivo .csv
        except:
            colunas = ['Nome', 'Idade', 'Gênero', 'Resposta_1', 'Resposta_2',
                       'Resposta_3', 'Resposta_4', 'Resposta_5', 'Data_e_hora']
            arquivo = pd.DataFrame(columns=colunas)
            arquivo.to_csv('resultados.csv', index=False)
            return self.verificarCsv()

    # receber as informações da lista de dicionários e adicionar ao arquivo .csv
    def pyToCsv(self, respostas):
        dados = self.verificarCsv()
        dados = dados.append(respostas, ignore_index=True)
        dados.to_csv('resultados.csv', index=False)
