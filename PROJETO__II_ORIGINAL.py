def tracinho():
    print("-"*130)

def espaco():
    print(" "*130)

tracinho()
print(f"Mapa sobre a Exclusão Digital no Brasil".upper().center(130))
print("-"*130)

import datetime

class Entrevistado:
    def __init__(self, nome, idade, genero, pergunta_2, pergunta_4):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.pergunta_2 = pergunta_2
        self.pergunta_4 = pergunta_4

## MÉTODO VAI DA LINHA 21 À 43
    def pergunta2(self):
        self.pergunta_2 = pergunta2

        if self.pergunta_2 == str(1):
            print(f"Sim")
        elif self.pergunta_2 == str(2):
            return "Não"
        elif self.pergunta_2 == str(3):
            return "Não sei dizer"
        
        return pergunta2
    
        #return self.nome = datetime.datetime(2022, 22, 7, 0)
    def pergunta4(self):
        self.pergunta_2 = pergunta4

        if self.pergunta_2 == str(1):
            print(f"Sim")
        elif self.pergunta_2 == str(2):
            return "Não"
        elif self.pergunta_2 == str(3):
            return "Não sei dizer"
        
        return pergunta4

pergunta2 = str(input("""
        Você acha que empresas como a Resilia,
        focadas no ensino da tecnologia e empregabilidade, ajudam a
        diminuir a Exclusão Digital no Brasil? 

        [1] Sim
        [2] Não
        [3] Não sei dizer
        Digite:   """))

pergunta4 = str(input("""
        Você acha que negros e pardos têm menos acesso 
        à internet e à inclusão digital no Brasil? 

        [1] Sim
        [2] Não
        [3] Não sei dizer
        Digite:   """))

resposta_2 = Entrevistado("Antônia", "18 anos", "Feminino", pergunta2, pergunta4)
print(resposta_2.pergunta2())
print(resposta_2.pergunta4())

### USEI DATETIME(ANO, MES, DIA, HORA, MINUTOS, SEGUNDOS)
resposta = datetime.datetime(2022, 7, 24, 7, 22, 9)
print(resposta)

# ABAIXO, FORMATANDO A DATA PARA DD/MM/AAAA E HORARIO EM (HORA, MINUTO, SEGUNDO)
hoje = datetime.datetime.today()
horario_de_brasilia = hoje.strftime("%d/%m/%Y")
print(horario_de_brasilia) ## Terminal --> 23/07/2022



resposta = datetime.datetime(2022, 7, 24, 7, 22, 9)
print(resposta)

#### Data e Hora atualizada em que a pergunta foi realizada
hoje = datetime.datetime.today()
horario_de_brasilia = hoje.strftime("%d/%m/%Y")
print(horario_de_brasilia) ## Terminal --> 23/07/2022