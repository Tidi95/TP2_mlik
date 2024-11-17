import string

def crypt(message, pas):

    if not 1 <= pas <= 9:
        raise ValueError("Le pas doit être compris entre 1 et 9")

    caracteres = string.ascii_letters + string.digits + " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    resultat = ""
    for caractere in message:
        indice = caracteres.find(caractere)
        if indice != -1:
            indice = (indice + pas) % len(caracteres)
            resultat += caracteres[indice]
        else:
            resultat += caractere
    return resultat + str(pas)

# Exemple d'utilisation :
message = "Hello, world!"
message_crypte = crypt(message, 3)
print(message_crypte)
