#!/usr/bin/python
#Steganography Basic
# -*- coding: ascii -*-

import platform, os, sys

if __name__ == "__main__":
    if platform.system() == "Windows":
        try:
            if sys.argv[1] == "--encryptar":
                nome = sys.argv[2]
                mensagem = sys.argv[3]
                nomefinal = sys.argv[4]
                if (".jpg") not in nome or (".png") not in nome:
                    os.system ("cls")
                    print ("Extensão incorreta, você deve informar uma imagem, e você informou:", nome)
                if (".txt") not in mensagem:
                    os.system ("cls")
                    print ("Extensão incorreta, você deve informar um txt/bloco de notas, e você informou:", mensagem)
                if (".jpg") not in nomefinal or (".png") not in nomefinal:
                    os.system ("cls")
                    print ("Extensão incorreta, você deve informar uma imagem, e você informou:", nomefinal)
                os.system ("cls && " + "copy /b "+nome+"+ "+mensagem+" "+nomefinal)
                print ("\n")
                os.system ("color b")
                print ("Terminado! Sua mensagem foi escondida em:",nomefinal)
                print ("Para ler a mesma, abra a imagem com um editor de texto, e vá ate a ultima linha..")
        except IndexError:
            def main():
                os.system("cls")
                os.system ("mode 110,40")
                print ("\n")
                print ("Como usar:")
                print ("\npython Steganograpy.py --encryptar nomearquivo.jpg mensagem.txt nomefinal.jpg")
                print ("\n--encryptar: Opção de encryptar mensagem dentro de imagem.")
                print ("\nApós o encryptar, você coloca o nome da imagem {nomearquivo.jpg} que você quer esconder a mensagem.")
                print ("\nDepois,{mensagem.txt}, você importa o TXT com a mensagem. Crie um .txt, digite uma mensagem e salve.")
                print ("\nE Por ultimo, nome final.")
                print ("No total, devem ser 4 argumentos.")
                print ("\npython Steganography.py --encrypt nomeimagem.jpg mensagem.txt nomefinal.jpg")
            main()
    if platform.system() == "Linux":
        try:
            if sys.argv[1] == "--encryptar":
                nome = sys.argv[2]
                mensagem = sys.argv[3]
                nomefinal = sys.argv[4]
                if (".jpg") not in nome or (".png") not in nome:
                    os.system ("clear")
                    print ("Extensão incorreta, você deve informar uma imagem, e você informou:", nome)
                if (".txt") not in mensagem:
                    os.system ("clear")
                    print ("Extensão incorreta, você deve informar um txt/bloco de notas, e você informou:", mensagem)
                if (".jpg") not in nomefinal or (".png") not in nomefinal:
                    os.system ("clear")
                    print ("Extensão incorreta, você deve informar uma imagem, e você informou:", nomefinal)
                os.system ("clear && " + "echo "+ mensagem + "> "+ nomefinal) 
                print ("\n")
                
                print ("Terminado! Sua mensagem foi escondida em:",nomefinal)
                print ("Para ler a mesma, abra a imagem com um editor de texto, e vá ate a ultima linha..")
        except IndexError:
            def main():
                os.system("clear")
                print ("\n")
                print ("Como usar:")
                print ("\npython Steganograpy.py --encryptar nomearquivo.jpg mensagem.txt nomefinal.jpg")
                print ("\n--encryptar: Opção de encryptar mensagem dentro de imagem.")
                print ("\nApós o encryptar, você coloca o nome da imagem {nomearquivo.jpg} que você quer esconder a mensagem.")
                print ("\nDepois,{mensagem.txt}, você importa o TXT com a mensagem. Crie um .txt, digite uma mensagem e salve.")
                print ("\nE Por ultimo, nome final.")
                print ("No total, devem ser 4 argumentos.")
                print ("\npython Steganography.py --encrypt nomeimagem.jpg mensagem.txt nomefinal.jpg")
            main()

