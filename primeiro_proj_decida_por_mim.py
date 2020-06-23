#Decida por mim
'''Objetivos: 
Seu programa deve permitir que o usuário faça uma pergunta para o programa, seu programa deve exibir na tela que está pensando(isso deve tomar alguns segundos) e depois o programa deve responder o usuário, dentro de 10 possibilidades que você criou para ele. Depois de exibir a resposta, você deve perguntar ao usuário se ele quer fazer outra pergunta. Caso ele responda positivamente rode o programa novamente e continue rodando desde que o usuário responda positivamente. Caso ele responda não. Finalize o programa e deixe uma mensagem agradecendo o usuário por usar seu programa.

Dicas iniciais:
Conceitos que podem ser usados:
Random / listas / Classes / Funções / print
'''

from time import sleep
import random

class RespondendoPerguntas():
    def __init__(self):
        self.resp = ["Você está certo disso!", "Você é que sabe!", "Neste momento não tenho resposta para a sua pergunta", 
                     "Você deve seguir a sua intuição!", "Eu também não gosto..", "Tenho a certeza que sim", "Sinceramente... sem comentários",
                    "Vou fazer de conta que você, não me fez essa pergunta", "A seu tempo as coisas irão se resolver", "Tente jogar no  Euromilhões", "Tens que obedecer aos teus pais", "A melhor resposta, esta em nossos corações"]
            
    def pergunta(self):
        
        input ("Faça uma pergunta?\n")
        print ("Estamos a processar a sua pergunta...\nAguarde!!!")
        sleep(3)
        print (random.choice(self.resp))
        
        continuar = input ("Deseja fazer outra pergunta? (S/N)\n")
        if continuar == "s":
            self.pergunta()
        elif continuar == "n":
            print ("Obrigado por utilizar nosso programa!")
        else :
            print ('Insira apenas "s" ou "n"')
            self.pergunta()

perguntar = RespondendoPerguntas()
perguntar.pergunta()