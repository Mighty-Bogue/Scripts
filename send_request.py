import socket # permet de travailler avec des sockets, qui sont des points de communication permettant d'établir des connexions réseau.

Rhost = "127.0.0.1" # IP de la cible
Directory = ".ssh"
Rport = 80 # Port de la cible
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création du socket

# Connexion vers la cible
socket.connect((Rhost,Rport))  

# Datas envoyées
request = "GET /%s/ HTTP/1.1\r\nHost:%s\r\n\r\n" % (Directory, Rhost)
socket.send(request.encode()) # Utilise la méthode send de l'objet socket, qui est une socket réseau. La méthode encode() est utilisée pour convertir la chaîne de caractères request en une séquence d'octets, car les sockets envoient des données sous forme d'octets.
print("data sent:\r\n"+request)

# datas reçues
response = socket.recv(4096) # Utilise la méthode recv() de l'objet socket pour recevoir des données du serveur distant. Plus précisément, elle essaie de recevoir jusqu'à 4096 octets (4 ko) de données depuis la connexion. Le résultat de cette opération est stocké dans la variable response
http_response = repr(response) #  Une fois les données reçues, on utilise la fonction repr() pour convertir le contenu de response en une représentation sous forme de chaîne de caractères (string).
http_response_len = len(http_response) # Calcule la longueur (en nombre de caractères) de la chaîne http_response résultant de l'étape précédente. Cela permet de déterminer la taille de la réponse HTTP reçue du serveur. Connaître la longueur de la réponse peut être important pour gérer correctement les données ou effectuer des opérations ultérieures.

# Affiche la réponse reçue
print("response lenght is : " + str(http_response_len))
print("The answer is :\r\n"+http_response)
