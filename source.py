# here, i will start typing the mannual code for scanning a wifi for devices by scanning IP addresses and ping them for response
# if no response then no device connected to this IP ... and so on with the range of the IPs given to the code to process
# for the main LAN project I'll be using scapy library for scanning as it is more reliable!

import socket
import ipaddress
import subprocess
import threading
import re
import time
import requests
from dotenv import load_dotenv
import os

# Get local IP of the device wanting to communicate and subnet
# you can do this in many ways I'm going to use one and comment the other

def configure():
    '''set a proper configuration'''
    load_dotenv()

def get_vendor(mac: str, token) -> str:
    '''sending mac address to Vendor API to get the type of the device discovered via its IP'''
    url = f"https://api.macvendors.com/{mac}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        return "Vendor not found / Request failed"
# this method uses public API and requires a registration which I think its a little bit exposed to share unique info with.
# so i will only send the first 6 digits

def get_local_ip():
    '''Option 1: creating a socket to connect to a public IP so that the 
    socket itself uses the local IP to maintain a dummy connection 
    (similar to connecting to 'www.google.com' server)'''

    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP connection
    conn.connect(('8.8.8.8', 80))

    local_ip = conn.getsockname()[0]

    # option 1 ended ;>

    # '''Option 2: using subprocess to get the IP address from the 
    #     command and depending on the system 
    #     you can use the right command'''

    # result = subprocess.run(['ip','addr'], capture_output=True, text=True)# use 'ipconfig' for windows
    # ip_pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    # ips_list = ip_pattern.findall(result.stdout.strip())
    # for ip in ips_list:
    #     if ip > '127.0.0.1': # exclude localhost so the scanning does not loop for the same device
    #         local_ip = ip
    #         break

    # # Option 2 ended ;>
    return local_ip

# Define ping function
def ping(ip):
    '''send pings (ICMP) commands to detect active ips two times in case of rejection the first time'''
    for _ in range(2):
        result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)],
                                stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"[+] Active: {ip}")
            break


# main

if __name__ == '__main__':
    
    token = os.getenv("token")
    
    local_ip = get_local_ip()

    network = ipaddress.ip_network(local_ip + '/24', strict=False)

    print(f"Scanning Network: {network}\n")
    
    start = time.perf_counter()
    # Loop through IPs using threads
    for ip in network:
        threading.Thread(target=ping, args=(ip,)).start()
    end = time.perf_counter()
    
    print(f"Finished Scanning succefully. Duration: {(end - start):.02f}s")

