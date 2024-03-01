import socket

# Création du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# age pour le port
age = 22

# Connexion au serveur sur localhost et le port 50 000 + age
server_address = ('localhost', 50000 + age)
client_socket.connect(server_address)

try:
    # Récupération du prénom de l'utilisateur
    prenom = input("Quel est votre prénom ? ")
    # Message envoyé au serveur
    request = f"Serveur es-tu là, tu vas bien, je m’appelle {prenom} ?"
    # Envoi de la requête initiale au serveur
    client_socket.send(request.encode('utf-8'))

    # Réception de la réponse du serveur à la requête initiale
    response = client_socket.recv(1024).decode('utf-8')
    print("Réponse du serveur:", response)

    while True:
        # Input pour l'utilisateur
        message = input("Entrez une commande(/date), ou la phrase magique : ")

        # Envoie du texte au serveur
        client_socket.send(message.encode('utf-8'))

        # Réception de la réponse du serveur
        response = client_socket.recv(1024).decode('utf-8')
        print("Réponse du serveur:", response)

        # Vérification si l'utilisateur veut terminer la connexion
        if message.strip() == "je suis a laeropor bisouuuu je manvol":
            print("Connexion terminée.")
            break

finally:
    # Fermer la connexion
    client_socket.close()
