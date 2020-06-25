#Simulador de Dado
'''
Objetivo: 
SEu programa deve: Gerar um número aleatório entre 1 a 6 (ou qualquer outro valor, mínimo e máximo) e exibir na tela. Depois disso deve perguntar ao usuário se ele quer rodar o dado novamente. Caso ele diga que sim gere e exiba um valor novo. Caso o usuário não responda a pergunta corretamente, mostre na tela quais as opções válidas e pergunte novamente se ele gostaria de rodar o dado.
'''
import random
from time import sleep

class jogar_dado:
         
    def continuar (self):
        question = input ("Seja bem vindo, Vamos Jogar? (s/n)")
        if question == "s":
            print (random.randint(1,6))
        while question == "s":
            question = input ("Vamos Jogar Novamente? (s/n)")
            print (random.randint(1,6))
        if question == "n":
            print ("Obrigado por ter jogado Aqui!")
        else:            
            print ("Insira uma resposta válida! 's' para SIM e 'n' para NÂO.")
            Jogar.continuar()
        
Jogar = jogar_dado()
Jogar.continuar()