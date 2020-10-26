# Simulador de dados
# Simula o uso de um dado, gerando um valor de 1 até 6

import random
import PySimpleGUI as sg

class SimuladorDado:
    def __init__(self):
        self.valorMin = 1
        self.valorMax = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
        
    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de dado', Layout=self.layout)
        # Ler os valores na tela
        self.eventos, self.valores = self.janela.read()
        # Fazer alguma coisa com esses valores
        try:
            if self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'n':
                print('Saindo...')
            else:
                print('Opção inválida')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    
    def GerarValorDoDado(self):
        print(random.randint(self.valorMin, self.valorMax))

simulador = SimuladorDado()
simulador.Iniciar()