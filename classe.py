import pandas as pd

class Entrevistador():
    aceite = bool
    nome = ''
    idade = 0
    sexo = ''
    resposta1 = ''
    resposta2 = ''
    resposta3 = ''
    resposta4 = ''

    def desejaParticipar(self):
        aceite = input('Você aceita participar dessa pesquisa? ')
        if aceite.upper() == 'SIM':
            return True
        elif aceite.upper == 'NÃO':
            return False
    
    def dadosBasicos(self):

        return # nome, idade, sexo

    def pergunta1(self):
        return  # resposta 1: 1-Sim, 2-Não, 3-Não Sei
    
    def pergunta2(self):
        return  # resposta 2: Sim, Não, Não Sei

    def pergunta3(self):
        return  # resposta 3: Sim, Não, Não Sei

    def pergunta4(self):
        return  # resposta 4: Sim, Não, Não Sei
    
    def reunirRespostas(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4):
        return #dicionário Respostas
    
    def pyToCSV(self, respostas):
        return #arquivo csv
    
    
    

         