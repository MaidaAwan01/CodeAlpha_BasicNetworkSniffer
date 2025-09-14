from scapy.all import sniff

# Packet handler function
def packet_capture(packet):
    print("📡 Packet captured:")
    if packet.haslayer("IP"):
        print(f"Source IP: {packet['IP'].src}")
        print(f"Destination IP: {packet['IP'].dst}")
        print(f"Protocol: {packet['IP'].proto}")
    if packet.haslayer("TCP") or packet.haslayer("UDP"):
        print(f"Payload: {str(packet.payload)}")
    print("-" * 50)

# Start sniffing (capture 10 packets only for demo)
print("Starting packet sniffer...")
sniff(count=10, prn=packet_capture)
