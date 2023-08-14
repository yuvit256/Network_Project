from scapy.all import rdpcap
import numpy as np
import matplotlib.pyplot as plt

def plot_inter_message_delays(pcap_path):
    # Load pcap file using scapy
    packets = rdpcap(pcap_path)
    
    # Calculate inter-message delays (time between successive packets)
    time_stamps = [packet.time for packet in packets]
    inter_message_delays = np.array(np.diff(time_stamps), dtype=float)  # Explicitly convert to float
    
    # Plot histogram of inter-message delays
    plt.hist(inter_message_delays, bins=50, density=True, alpha=0.7, label="Histogram of Inter Message Delays")
    
    # Fit an exponential distribution to the data
    lambda_exp = 1.0 / np.mean(inter_message_delays)
    x = np.linspace(0, max(inter_message_delays), 1000)
    y = lambda_exp * np.exp(-lambda_exp * x)
    
    # Plot the fitted exponential distribution
    plt.plot(x, y, label="Fitted Exponential Distribution", color="red")
    
    # Set plot labels and title
    plt.xlabel("Inter Message Delays (Seconds)")
    plt.ylabel("Probability Density Function (PDF)")
    plt.title("PDF of Inter-Message Delays and its Fitted Exponential Distribution")
    plt.legend()
    
    plt.show()

plot_inter_message_delays("file_path")
