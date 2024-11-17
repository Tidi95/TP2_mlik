import string

def crypt(message):
    caracteres = string.ascii_letters + string.digits + " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + " "
    resultat = ""
    for caractere in message:
        indice = caracteres.find(caractere)
        # On gère le cas où le caractère n'est pas dans notre liste
        if indice != -1:
            indice = (indice + 1) % len(caracteres)
            resultat += caracteres[indice]
        else:
            resultat += caractere
    return resultat

print(crypt("Hello, world!"))
