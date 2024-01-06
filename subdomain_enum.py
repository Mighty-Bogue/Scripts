# Importation du module sys pour accéder aux arguments de ligne de commande.
import sys
# Importation du module requests pour effectuer des requêtes HTTP.
import requests

# Ouverture et lecture du fichier wordlist passé en premier argument de la ligne de commande.
# La méthode .read() lit tout le contenu du fichier et le stocke dans la variable wordlist.
wordlist = open(sys.argv[1]).read()

# La boucle parcourt chaque caractère du contenu du fichier wordlist
for sub in wordlist:

    # Formation du sous-domaine en ajoutant le sous-domaine actuel à l'argument de domaine.
    # La f-string (f"") est utilisée pour formater la chaîne avec les valeurs des variables.
    subdom = f"http://{sub}.{sys.argv[2]}"

    # Tentative d'envoi d'une requête GET à l'URL du sous-domaine formé.
    try:
        requests.get(subdom)
    
    # Gestion de l'exception en cas d'erreur de connexion.
    # Si une erreur de connexion se produit (par exemple, le sous-domaine n'existe pas ou ne répond pas), l'exception requests.ConnectionError est capturée et le code passe à l'instruction suivante.
    except requests.ConnectionError: 
        pass
    
    # Si la requête est réussie (c'est-à-dire si le sous-domaine est valide et répond à la requête GET), l'instruction suivante est exécutée pour afficher le sous-domaine valide.
    else:
        print("Valid domain: ", subdom)
