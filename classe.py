import pandas as pd

class Entrevistador():
    
    def __init__(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.resposta1 = resposta1
        self.resposta2 = resposta2
        self.resposta3 = resposta3
        self.resposta4 = resposta4
        self.resposta5 = resposta5

    def desejaParticipar(self):
        aceite = input('Você aceita participar dessa pesquisa? ')
        if aceite.upper() == 'SIM':
            return True
        elif aceite.upper == 'NÃO':
            return False
    
    def dadosBasicos(self):

        return # nome, idade, sexo

    def pergunta1(self):
        return  # resposta 1: 1-Sim, 2-Não, 3-Não Sei # laura
    
    def pergunta2(self):
        return  # resposta 2: Sim, Não, Não Sei

    def pergunta3(self):
        return  # resposta 3: Sim, Não, Não Sei

    def pergunta4(self):
        return  # resposta 4: Sim, Não, Não Sei

    def pergunta5(self, resposta5):
        if resposta5 == 1:
            self.resposta5  = "Sim"
            return self.resposta5
        elif resposta5 == 2:
            self.resposta5  = "Não Sei"
            return self.resposta5
        elif resposta5 == 3:
            self.resposta5 = "Não"
            return self.resposta5
           
    
    def reunirRespostas(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5):
        resposta = {nome : [idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5]}
        return resposta
    
    def pyToCSV(self, respostas):
        return #arquivo csv
    
    
    

         