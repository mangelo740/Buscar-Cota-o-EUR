from tkinter import N
import requests
import time
import pygame



# CONEXÃO COM API DE MERCADO
#requisicao = requests.get("https://www.googleapi.com/finance/quote/EUR-BRL")
requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
cotacao = requisicao.json()

print('-' * 35)
print("ROBÔ - AVISA QUANDO A COTAÇÃO É BOA")


# VARIAVEIS DE CONTROLE
print('-' * 35)
segundos = int(input('Em quantos segundos atualizar? '))
meta = float(input("Cotação desejada da moeda? "))
print('-' * 35)
valor = float(cotacao['EUR']['bid'])


# REPETIÇÃO ATÉ CHEGAR NA META
while valor >= meta:
    print('-' * 35)
    print('#### Cotação do Euro ####')
    print('-' * 35)
    print ('Moeda: ' + cotacao['EUR']['name'])
    print ('Data: ' + cotacao['EUR']['create_date'])
    print('-' * 35)
    print('Valor atual: R$' + cotacao['EUR']['bid'])
    time.sleep(segundos)


# ALARME DE A META FOR ATINGIDA
pygame.mixer.init()
pygame.mixer.music.load('.\sample.mp3')
pygame.mixer.music.play()

print('-' * 35)
print(f'A sua meta de cotação foi atingida {meta} a cotação atual é {valor}') 
print('-' * 35)


# SAÍR DO PROGRAMA
sair = int(input("Digite 1 para sair: "))

if sair == 1:
    print('Obrigado por utilizar o programa de aviso')

