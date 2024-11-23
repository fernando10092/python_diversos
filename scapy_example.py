from scapy.all import *

# Criação de um pacote IP com ICMP
packet = IP(dst="www.google.com.br") / ICMP()

# Envia o pacote e espera a resposta
response = sr1(packet, timeout=2)

# Exibe os detalhes da resposta
if response:
    response.show()
else:
    print("Nenhuma resposta recebida.")
