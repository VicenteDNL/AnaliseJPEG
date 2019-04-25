
'''
Referencia de pesquisa: https://www.file-recovery.com/jpg-signature-format.htm

Obs:Ele não tem um comprimento do arquivo incorporado

'''

#Ler a Imagem
import binascii
im = open("image.jpeg","rb")
data= im.read()
im.close

#Salva a imagem e converte em Hexadecimal em um arquivo TXT
im=open("Hexadecimal.txt","wb",)
im.write(binascii.hexlify(data))
im.close()

#Abre o arquivo txt para leitura, e salva em variavel
im=open("Hexadecimal.txt","r",)
hexadecimal =im.read()
im.close()

#Verifica se a imagem é JPEG
def isJPEG(hexadecimal):
    if (hexadecimal[:6].lower() == "ffd8ff"):
        return True
    else:
        return False


print("A IMAGEM É JPEG? : " + str(isJPEG(hexadecimal)))
