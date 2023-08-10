# Network_Project
## In this assignment we wrote plot.py. 
### Running the code: to run the code, you need to change
line 31 to the path of your pcap file and then you are good to go.
We opened 6 WhatsApp groups called: videos, recordings, files, photos, text and everything from everything. In each group we sent its description with some text in between.
How it works: one sent the messages to each group when in each group we sent a different type of messages while the other recorded the traffic and filtered it according to:
tcp.port==433 and tls which means we filter according to port 433 which is used for encrypted traffic and also the tls protocol is used to transfer encrypted information exactly like this information is transferred in WhatsApp.
Each recording took between 4-6 minutes and then we stopped the recording and saved it.
Then we wrote a code in python that receives the location of the recording and turns it into a graph of the size of the packet in bytes as a function of time in seconds.
This part was performed twice, once with clean recordings and then recordings with background noise.
## Authers: Ron Yacobovich & Yuval Musseri
