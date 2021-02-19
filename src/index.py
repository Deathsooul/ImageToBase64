import base64


with open('./assets/paisagem.jpg', 'rb') as img_file:
    string = base64.b64encode(img_file.read())

#Retirando o prefixo do base64

print(string.decode('utf-8'))