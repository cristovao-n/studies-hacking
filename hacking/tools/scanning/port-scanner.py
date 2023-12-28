import socket
from termcolor import colored

def handle_ports_range(portsRange):
  ports = []
  for portRange in portsRange:
    leftInterval = portRange.split("-")[0]
    rightInterval = portRange.split("-")[1]
    for i in range(int(leftInterval), int(rightInterval)+1):
      ports.append(i)
  return ports

def scan_targets(targets, ports):
  for target in targets:
    print(colored("\nScanning target " + target, "blue"))
    scan_target_ports(target, ports)

def scan_target_ports(target, ports):
  for port in ports:
    scan_target_port(target, port)

def scan_target_port(target, port):
  try:
    sock = socket.socket()
    sock.connect((target, port))
    print("[+] Port Opened " + str(port))
    sock.close()
  except:
    pass

targetsInput = input("[A,B] Enter the targets you want to scan separated by comma: \n")
portsInput = input("[1-100,300-500] Enter the ports you want to scan: \n")

targets = targetsInput.split(",")
portsRange = portsInput.split(",")

ports = handle_ports_range(portsRange)

scan_targets(targets, ports)
