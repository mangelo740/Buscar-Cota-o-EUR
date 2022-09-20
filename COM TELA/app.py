import requests
import time
import pygame
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_untitled import *


def main(ui):
    def executar():
        primeiro()
        bolsa()


    def primeiro():
        # CONEXÃO COM API DE MERCADO
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
        cotacao = requisicao.json()
        valor = float(cotacao['EUR']['bid'])
        valorstr = str(valor)


        msg1 = ('Moeda: ' + cotacao['EUR']['name'])
        msg1_1 = str(msg1)
        ui.lmsg1.setText(msg1_1)
        msg2 = ('Data: ' + cotacao['EUR']['create_date'])
        ui.lmsg2.setText(msg2)
        msg3 = ('Valor atual: R$' + cotacao['EUR']['bid'])
        ui.lmsg3.setText(msg3)



    def bolsa():
        # CONEXÃO COM API DE MERCADO
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
        cotacao = requisicao.json()


        # VARIAVEIS DE CONTROLE
        segundos = int(ui.lsegundo.text())

        # TIVE QUE CONVERTER A INFORMAÇÃO DE STR PARA FLOAT
        meta = ui.lmeta.text()
        meta1 = meta.replace(",", ".")
        meta2 = float(meta1)
        valor = float(cotacao['EUR']['bid'])


        # REPETIÇÃO ATÉ CHEGAR NA META
        while valor > meta2:
            print('Moeda: ' + cotacao['EUR']['name'])
            print('Data: ' + cotacao['EUR']['create_date'])
            print('Valor atual: R$' + cotacao['EUR']['bid'])
            
            msg1 = ('Moeda: ' + cotacao['EUR']['name'])
            msg1_1 = str(msg1)
            ui.lmsg1.setText(msg1_1)

            msg2 = ('Data: ' + cotacao['EUR']['create_date'])
            msg2_2 = str(msg2)
            ui.lmsg2.setText(msg2_2)

            msg3 = ('Valor atual: R$' + cotacao['EUR']['bid'])
            msg3_3 = str(msg3)
            ui.lmsg3.setText(msg3_3)


            time.sleep(segundos)


        # ALARME DE A META FOR ATINGIDA
        pygame.mixer.init()
        pygame.mixer.music.load('.\sample.mp3')
        pygame.mixer.music.play()
        

    ui.pushButton.clicked.connect(executar)

 


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())