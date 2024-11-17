import string

import string

def crypt(message, pas):
    """Crypte un message en décalant chaque caractère d'un nombre de positions donné dans la table ASCII.

    Args:
        message (str): Le message à crypter.
        pas (int): Le nombre de positions de décalage (entre 1 et 9).

    Returns:
        str: Le message crypté avec le pas concaténé à la fin.
    """

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
    return resultat

# Exemple d'utilisation :
message = "Hello, world!"
message_crypte = crypt(message, 3)
print(message_crypte)
message_decrypte = decrypt(message_crypte)
print(message_decrypte)

