from scapy.all import IP, ICMP, send,sr1

# Create an IP packet with an ICMP layer
packet = IP(dst="8.8.8.8") / ICMP()

# Send the packet
send(packet)
response = sr1(packet, timeout=2)
if response:
    print("Reply received:")
    response.show()
else:
    print("No reply (timeout)")
