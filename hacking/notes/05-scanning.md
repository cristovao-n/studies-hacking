# Scanning

We'll use free vulnerable virtual machines for study porpuses
We'll fetch information about the technologies the target uses.

We'll look for open ports in the target

- 21: ftp
- 22: ssh
- 25: smtp
- 53: dns
- 80: http
- 443: https

If there's a vulnerable software running in one of these open ports, then the target is vulnerable

Our goal is to find open ports and exploit the target that runs vulnerable software on that open port.

## Vulnerable Virtual Machine

Search for a vulnerable machine in google and run it on VirtualBox.

Example: Metasploitable

## Firewalls

Firewall is a network security system that monitors network traffic based on the security rules pre-determined.

There are two types of firewalls:

- Network Firewalls: Filters traffic between two or more networks
- Host-based Firewalls: Filter traffic that goes in or out that specific host

## IDS: Intrusion Detection Service

A software application that monitors network for any malicious activity
Some nmap scans can get caught by IDS

### Finding hosts

`sudo arp -a` -> ARP table
`sudo netdiscover` -> Find hosts in the local network
`nmap -sn 192.168.1.1-255` -> Find hosts in the local network
`netstat -nr` -> Find the router ip

### nmap

Nmap is a very important tool for scanning

#### Finding open ports in a host:

`nmap {HOST}`

> There are more advanced, aggressive scans that returns more information.
> Documentation for the most commom commands of nmap CLI
> https://zerotomastery.io/cheatsheets/nmap-cheat-sheet/?utm_source=udemy&utm_medium=coursecontent

#### Commons scans

`nmap -sS {HOST}`
`nmap -s`

#### Discovering target OS

The target machine must have at least one port open and one port closed.

OBS: The MAC Address of VMs starts with `08:00:27`

`sudo nmap -O {HOST}`

#### Detecting versions of services

`sudo nmap -sV {HOST}`

`sudo nmap -sV --version-intensity 0-9 {HOST}`

#### Aggressive scam

This is easily detected by the target if it has good security artifacts.

`sudo nmap -A {HOST}`

#### Scan port range

This is useful when you want to be stealthy and scan just a few ports

`nmap -p PORT {HOST}`
`nmap -p 80, 22, 100 {HOST}`
`nmap -p 1-100 {HOST}`

Scans all 2^16 ports available: `nmap -p 1-65535 {HOST}`
Scans the most used 100 ports: `nmap -F {HOST}`

#### Bypassing Firewalls

Packet fragmentation

`sudo nmap -f {HOST}`

#### Decoys

Target is in the same network - send fake packages from random local IP address to hide the real one

`sudo nmap -D 192.168.1.2, 192.168.1.5, 192.168.1.15, ME {HOST}`

Target is outside your network - send fake packages from random IP address to hide the real one

`sudo nmap -D RND:5 HOST`
