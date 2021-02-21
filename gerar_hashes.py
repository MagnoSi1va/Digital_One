import hashlib
string = input("Digite o texto ou número a ser encryptado: ")
menu = int(input(''' ### MENU- ESCOLHA O TIPO DE HASH ###
            1) MD5
            2) SHA1
            3) SHA256
            4) SHA512
            DIGITE O NÚMERO A QUE CORRESPONDE A CRIPTOGRAFIA DESEJADA: '''))
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A Hash MD5 gerada apartir de: ', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A Hash SHA1 gerada apartir de: ', string, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A Hash SHA256 gerada apartir de: ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('A Hash SHA512 gerada apartir de: ', string, 'é: ', resultado.hexdigest())
else:
    print("Algo de Errado não está certo. Tente novamente!!!")