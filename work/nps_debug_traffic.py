import scapy.all as scapy

request_packets = []


def sniff_packets(iface=None):
    if iface:
        scapy.sniff(filter="port 1812", prn=process_packet, iface=iface, store=False)
    else:
        scapy.sniff(filter="port 1812", prn=process_packet, store=False)


def process_packet(packet):
    if packet.haslayer('Radius'):
        if packet['Radius'].code == 1:
            print(f"Received {packet.sprintf('%Radius.code%')} packet with id: {packet['Radius'].id}")
            request_packets.append(packet['Radius'].id)
        else:
            print(f"Received {packet.sprintf('%Radius.code%')} packet with id: {packet['Radius'].id}")
            if (packet['Radius'].id) in request_packets:
                request_packets.remove(packet['Radius'].id)


try:
    sniff_packets()
    print(request_packets)
except KeyboardInterrupt:
    if len(request_packets) == 0:
        print("Looks good, all packets were answered")
    else:
        print(f"Found unanswered packets with the following ids: {request_packets}")
