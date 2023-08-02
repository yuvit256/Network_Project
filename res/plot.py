import matplotlib.pyplot as plt
from scapy.all import rdpcap


def plot_packet_sizes(pcap_file):
    packets = rdpcap(pcap_file)
    packet_sizes = [len(packet) for packet in packets]

    plt.figure(figsize=(10, 6))
    plt.plot(packet_sizes, marker='o', markersize=3)
    plt.xlabel('Packet Index')
    plt.ylabel('Packet Size (bytes)')
    plt.title('Packet Sizes in PCAP')
    plt.grid(True)
    plt.show()
    

if __name__ == "__main__":
    pcap_file = "/home/yuval/Desktop/Python/nc_4/ws/hi.pcapng"
    plot_packet_sizes(pcap_file)    
