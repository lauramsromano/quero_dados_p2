import pandas as pd


class Entrevistado():

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
    def pergunta(self, resposta):
        if resposta == 1:
            self.resposta1 = "Sim"
            return self.resposta1
        elif resposta == 2:
            self.resposta1 = "Não"
            return self.resposta1
        elif resposta == 3:
            self.resposta1 = "Não sei responder"
            return self.resposta1

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

    #verifica se as respostas são numeros entre 1 e 3 :
    def validaResposta(self, resposta):
        while True:
            try:
                resposta = int(resposta)
                # checa se a resposta pode ser atribuida como inteiro
                if  resposta  < 1 or resposta > 3:
                    # testa se a resposta está fora intervalo aceitável, se tiver retorna o erro
                    raise ValueError ('Insira apenas números entre 1 e 3. ')
            except ValueError as e:
                print(e)
                resposta = input('Digite novamente: ')
            else:
                break
        return resposta
    
    def validaIdade(self, idade):
        if idade == 00:
            return idade
        while True:
            try:
                idade = int(idade)
                if idade < 00 or idade > 110:
                    raise ValueError ('Insira uma faixa atária válida, entre 1 e 110 anos. ')
            except ValueError as e:
                print(e)
                idade = input('Digite novamente: ')
            else:
                break
        return idade

            