import socket
from datetime import datetime

# Fonction pour trouver un port disponible
def find_port():
    age = 22
    port = 50000 + age
    while True:
        try:
            server_socket.bind(('localhost', port))
            print(f"Le serveur écoute sur le port {port}")
            break
        except OSError:
            print(f"Le port {port} est occupé, en recherche d'un autre port disponible...")
            port += 100

# Création du socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Trouver un port disponible
    find_port()

    # Activer le mode d'écoute du socket
    server_socket.listen(1)

    print("Le serveur est prêt ")

    # Accepter la connexion
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    try:
        while True:
            # Recevoir le message du client
            message = client_socket.recv(1024).decode('utf-8')
            print("Message reçu du client:", message)

            # Vérifier si le message est la commande "/date"
            if message.strip() == "/date":
                # Obtenir la date actuelle
                current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                response = f"Date actuelle : {current_date}"
                print("Réponse du serveur:", response)
            elif message.strip() == "je suis a laeropor bisouuuu je manvol":
                response = "Connexion terminée."
                print("Réponse du serveur:", response)
                break  # Sortir de la boucle while pour terminer la connexion
            else:
                response = message + " Je suis là !"
                print("Réponse du serveur:", response)

            # Renvoyer la réponse au client
            client_socket.send(response.encode('utf-8'))

    finally:
        # Fermer la connexion avec le client
        client_socket.close()

finally:
    # Fermer le socket serveur en cas d'erreur
    server_socket.close()
