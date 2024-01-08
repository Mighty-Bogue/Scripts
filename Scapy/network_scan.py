from scapy.all import *
import sys

# Interface et Range IP en arguement
interface = sys.argv[1]
ip_range = sys.argv[2]
broadcastMac = "ff:ff:ff:ff:ff:ff" # Adresse MAC de broadcast

print("\n!! Do not forget to be root or use sudo !!\n")

print("Usage ===> python <script_name>.py <Interface> <Network range>")
print("Example => python network_scan.py eth0 192.168.1.0/24\n")

# Création du paquet ARP encapsulé dans une trame Ethernet
packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 

# Envoi des paquets et récupération des réponses. On créé deux listes : answers et noanswers. En effet la fonction srp() retourne deux valeurs (une pour les paquets avec réponses et pour les paquets sans réponses).
answers, noanswers = srp(packet, timeout =2, iface=interface, inter=0.1)

#  Parcours les réponses reçues et affiche les adresses IP et MAC pour chaque réponse
for send,receive in answers:
        print (receive.sprintf(r"%ARP.psrc% => %Ether.src%")) 
