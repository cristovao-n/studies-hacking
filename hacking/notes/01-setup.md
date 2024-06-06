# Setup

## What is a virtual machine?

- It is a way to run a machine inside your physical machine
- It is a safe way to run another operating system in a physical machine
- The physical machine will borrow part of the hardware for the virtual machine to execute.

### Why to learn VMs?
- It's the secure way of learning hacking
- Learn other operating systems
- Break stuff

> **To create a virtual machine, we need two things:**
> - Operating System: Kali Linux
> - Virtualization Software: VirtualBox
>

---

## Creating a Kali Linux VM

The process is quite simple:
- Download the ISO image
- Create the VM alocating the desired amount of hardware resources
  - Version: Debian 64-bit
  - Base Memory: 4Gb 
  - Processors: 1 CPU
  - Hard Disk: 40Gb
- Follow the wizard

### Installing OS
- View -> Scale mode
- Hostname: kali
- Domain name: empty
- User: MrHacker, mrhacker, 15122021
- Clock: Eastern
- Partition disks: Guided - use entire disk
  - All files in one partition
- Software selection: default
- GRUB boot loader: Yes
  - /dev/sda
- Boot machine

### Settings

- Display -> Video Memory: 80Mb
- Installing Guest Additions
  - sudo sh VBoxLinuxAdditions.run

### Network settings

We should get an IP address from the router (DHCP)
To do this, just go to settings > network > attached to: Bridged Adapter

> If the internet doesn't work, ensure the MAC address of the VM is the same of the host OS
>

### Kali Linux setup

> **Swap ctrl and caps lock:**
> - put the command `/usr/bin/setxkbmap -option "ctrl:swapcaps"` into `~/.profile` file
>

> **Useful article:**
> https://www.ceos3c.com/security/top-things-after-installing-kali-linux/?expand_article=1
>

