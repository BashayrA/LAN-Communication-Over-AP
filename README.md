# LAN Device Scanner (Python)

A lightweight Python script for scanning devices on your local network. This tool helps identify active IP addresses within a subnet, making it useful for network diagnostics, device discovery, and future LAN communication setups.

## 🔍 What It Does

- Scans a specified subnet (e.g., `/24`) for active devices
- Uses socket and IP libraries to detect reachable IPs
- Prints out live IPs for further inspection or messaging
- Discover devices via its vendors using public API from [text](https://macvendors.com/). Make sure to use your own token if you choose this option to work with!

## 🚀 How to Use

1. Make sure you're connected to a local network
2. Run the script:
   ```bash
   python source.py

## 🧠 Project Vision

This scanner is the first step in a multi-stage project to build a LAN communication app.  
The final goal is to enable **offline messaging between devices** connected to the same **access point**, without relying on internet access.

## Next
The next step is to build a way to discover the types of connected devices using scapy

The broader project will include:
- Setting up the Raspberry Pi as a wireless AP
- Discovering and identifying connected devices
- Enabling direct and broadcast messaging over LAN
- Ensuring secure and efficient communication across the network

further editting and feature addition on the way!
