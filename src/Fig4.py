from scapy.all import rdpcap
import numpy as np
import matplotlib.pyplot as plt

def extract_packet_sizes(pcap_path):
    """Extract packet sizes from a pcap file using scapy."""
    packets = rdpcap(pcap_path)
    lengths = [len(packet) for packet in packets]
    return lengths

def compute_ccdf(data):
    """Compute the CCDF for a dataset."""
    sorted_data = np.sort(data)
    # CDF calculation
    cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    # CCDF is 1 - CDF
    ccdf = 1 - cdf
    return sorted_data, ccdf

# Paths to pcap files for different message types
pcap_paths = {
    'Text': '/home/yuval/Desktop/Network_Project-main/resources/texts.pcapng',
    'Video': '/home/yuval/Desktop/Network_Project-main/resources/videos.pcapng',
    'Image': '/home/yuval/Desktop/Network_Project-main/resources/images.pcapng',
    'File': '/home/yuval/Desktop/Network_Project-main/resources/files.pcapng',
    'Audio': '/home/yuval/Desktop/Network_Project-main/resources/audios.pcapng',
    'AllTypes': '/home/yuval/Desktop/Network_Project-main/resources/alltypes.pcapng'
}

# Extract packet sizes and compute CCDF for each message type
ccdf_data = {}
for message_type, pcap_path in pcap_paths.items():
    sizes = extract_packet_sizes(pcap_path)
    ccdf_data[message_type] = compute_ccdf(sizes)

# Plotting the CCDFs
plt.figure(figsize=(12, 6))
for message_type, (sorted_data, ccdf) in ccdf_data.items():
    plt.plot(sorted_data, ccdf, label=message_type)

plt.title('CCDF of IM Size distributions for different types of messages')
plt.xlabel('Message Size (bytes)')
plt.ylabel('Probability')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.grid(True)
plt.show()