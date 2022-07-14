
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.mensagem_inicial = 'Você gostaria de gerar um valor em dado? '
        self.mensagem_dados = 'Qual dado gostaria de rolar? '
        self.mensagem_quantidade = 'Quantos dados gostaria de rolar? '
    def Inciar(self):
        resposta = input(self.mensagem_inicial)
        
        if resposta == 'sim' or resposta == 's':
            self.valor_maximo = input(self.mensagem_dados)
            self.quantidade = int(input(self.mensagem_quantidade))
            if self.valor_maximo == 'd4':
                self.valor_maximo = 4
                self.GerarValorDoDado()
            elif self.valor_maximo == 'd6':
                self.valor_maximo = 6
                self.GerarValorDoDado()
            elif self.valor_maximo == 'd8':
                self.valor_maximo = 8
                self.GerarValorDoDado()
            elif self.valor_maximo == 'd10':
                self.valor_maximo = 10
                self.GerarValorDoDado()
            elif self.valor_maximo == 'd12':
                self.valor_maximo = 12
                self.GerarValorDoDado()
            elif self.valor_maximo == 'd20':
                self.valor_maximo = 20
                self.GerarValorDoDado()
            elif self.valor_maximo == 'd100':
                self.valor_maximo = 100
                self.GerarValorDoDado()
            else:
                print('os dados disponiveis são d4, d6, d8, d10, d12, d20 e d100. Porfavor selecione uma das opções ')
        elif resposta == 'não' or resposta == 'n':
            print('Agradecemos a sua participação! ')
        else:
            print('Por favor responda sim ou não')


    def GerarValorDoDado(self):
        res = []
        for j in range(self.quantidade):
            res.append(random.randint(self.valor_minimo, self.valor_maximo))
        print (f'O resultado da sua jogada é {sum(res)}')
        
simulador = SimuladorDeDado()
simulador.Inciar()
