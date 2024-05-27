import socket
from scapy.all import sniff, TCP, IP

# Dirección y puerto del servidor de Node.js
# Si lo desea puede ser cambiada a la que mas desee :D
SERVER_IP = '127.0.0.1'
SERVER_PORT = 65432

# Lista de IPs conocidas (puedes poner mas dependiendo de que queirias hacer :D)
known_ips = {
    "157.240.25.60",   # Facebook
    "3.212.150.249",   # AWS
    "172.64.146.98",   # Cloudflare
    "104.18.33.170",   # Cloudflare
    "140.82.112.25",   # GitHub
    "34.252.39.26",    # AWS
    "142.250.115.188", # Google
    "13.107.5.93"      # Microsoft
}

def send_alert(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        s.sendall(message.encode('utf-8'))

def packet_callback(packet):
    if IP in packet and TCP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        dport = packet[TCP].dport

        # En caso de que la ip no sea conocida 
        if ip_dst not in known_ips:
            alert_msg = f"Alerta: Conexión TCP inusual detectada desde {ip_src} hacia {ip_dst}:{dport}"
            print(alert_msg)
            send_alert(alert_msg)

def main():
    print("Iniciando captura de paquetes...")
    sniff(filter="tcp", prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
