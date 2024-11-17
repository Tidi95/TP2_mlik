import string

def decrypt(message):

    pas = int(message[-1])  # Récupérer le pas à partir du dernier caractère
    message = message[:-1]  # Supprimer le pas du message
    caracteres = string.ascii_letters + string.digits + " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    resultat = ""
    for caractere in message:
        indice = caracteres.find(caractere)
        if indice != -1:
            indice = (indice - pas) % len(caracteres)  # Décalage négatif pour décrypter
            resultat += caracteres[indice]
        else:
            resultat += caractere
    return resultatimport string

