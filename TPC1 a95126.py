# -*- coding: utf-8 -*-
"""
Created on Oct 2021

@author: Adriana Miranda
"""

#JOGO 21 FÓSFOROS

import random

def jogovinteeum ():
    print ("Bem-vindo ao jogo dos 21 fósforos.")
    print ("Neste jogo existem 21 fósforos e o objetivo é ir retirando entre 1 a 4 destes, o jogador vencedor será o que deixar o último fósforo.")
    x= input (""""Irá jogar contra o computador. Prefere ser o primeiro ou segundo jogador? Selecione:
           1 para primeiro jogador
           2 para segundo jogador
           """)
           
    b=21       
    if x=="1":
        while b>1:
            z=int(input("Retire um número de 1-4: "))
            if z<1 or z>4:
               print ("Erro, insira um número válido para jogar.")
            if z>=1 and z<=4:
               num_fosforos=b-z
               print ("Restam:", num_fosforos, "fósforos.")
               print ("O computador retirou", 5-z, "fósforos. Restam:", num_fosforos-(5-z), "fósforos.")
               b=b-5
        if b==1:
           print ("Você perdeu o jogo.")
               
               
            
           
    if x=="2":
        jogada_pc=random.randint(1,4)
        b=b-jogada_pc
        print ("O computador retirou:", jogada_pc, "fósforos. Restam:", b, "fósforos.")
        while b>1:
            z=int(input ("É a sua vez de jogar. Retire entre 1-4 fósforos:"))
            if z<1 or z>4:
                print ("Erro, insira um número válido para jogar")
            if z>=1 and z<=4:
                b=b-z
                print ("Restam", b, "fósforos.")
                if b==1:
                    print("Parabéns, ganhou o jogo!")
                if b==2:
                    jogada_pc=1
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    print("Você perdeu o jogo.")
                if b==3:
                    jogada_pc=2
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    print("Você perdeu o jogo.")
                if b==4:
                    jogada_pc=3
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    print("Você perdeu o jogo.")
                if b==5:
                    jogada_pc=4
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    print("Você perdeu o jogo.")
                if b==6:
                    jogada_pc=random.randint(1,4)
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==7:
                    jogada_pc=1
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==8:
                    jogada_pc=2
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==9:
                    jogada_pc=3
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==10:
                    jogada_pc=4
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==11:
                    jogada_pc=random.randint(1,4)
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==12:
                    jogada_pc=1
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==13:
                    jogada_pc=2
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==14:
                    jogada_pc=3
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==15:
                    jogada_pc=4
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==16:
                    jogada_pc=random.randint(1,4)
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==17:
                    jogada_pc=1
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==18:
                    jogada_pc=2
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==19:
                    jogada_pc=3
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                    
                if b==20:
                    jogada_pc=4
                    b=b-jogada_pc
                    print("O computador retirou:", jogada_pc, "fósforos.")
                    print("Restam", b, "fósforos.")
                             
     
jogovinteeum()