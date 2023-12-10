# Information Gathering

## Active Information Gathering

Information is gathered directly in the target

## Passive Information Gathering

Information is gathered with the help of a middle source
This source can be a person, a website, etc

---

## Getting IP address of the target

### Actively

#### ping

Just `ping` the target and you'll see the IP address as the packages are sent thanks to the DNS protocol.

#### nslookup

It returns the IP address of the target using DNS protocol.

#### whois

It returns more information about the target, such as the physical address, etc.

### Passively

- ipinfo website

---

## Whatweb

You can use this tool to identify what technologies a website uses, for example.
The default level of aggression, called _stealthy_, is the fastest and requires only one HTTP request. It is suitable for scanning public websites.
More aggressive modes were developed for use in penetration tests.

### Stealthy scan

`whatweb example.com`
`whatweb --verbose example.com`

### Aggressive scan

- local network

`whatweb 192.168.1.1-192.168.1.255 --aggresion 3 -v --no-errors`

---

## Gathering emails

### theHarvester

`theHarvester -d DOMAIN -b SOURCE`

### hunter.io

- website

## Searching for more tools in github

- Just search "Information Gathering Github"
  - sherlock
