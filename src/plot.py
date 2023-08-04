import matplotlib.pyplot as plt
from scapy.all import rdpcap

def plot_packet_sizes(pcap_file):
    # Read the packets from the PCAP file
    packets = rdpcap(pcap_file)

    # Extract packet sizes for each packet in the PCAP
    packet_sizes = [len(packet) for packet in packets]

    # Extract timestamps from each packet (assuming the packets have a 'time' field)
    timestamps = [packet.time for packet in packets]

    # Create a plot to visualize the packet sizes over time
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, packet_sizes, marker='o', markersize=3)

    # Set labels and title for the plot
    plt.xlabel('Time (seconds)')
    plt.ylabel('Packet Size (bytes)')
    plt.title('Packet Sizes in PCAP')

    # Enable grid lines on the plot
    plt.grid(True)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    # Path to the PCAP file
    pcap_file = "/home/yuval/Desktop/Python/nc_4/ws/hi.pcapng"
    # Call the function to plot packet sizes over time
    plot_packet_sizes(pcap_file)
