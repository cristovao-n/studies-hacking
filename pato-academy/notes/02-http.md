# HTTP Protocol

## HTTP/1.1

Request line  
Literal text encoding

### Request

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

## HTTP/2

New version of HTTP with performance improvements  
Request line replaced by meta headers  
Optimized encoding protocol instead of literal text encoding.

### Request

```
:method    GET
:scheme    https
:authority www.example.com
:path      /index.html
user-agent Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
accept     text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
accept-encoding gzip, deflate
```

# URL - Uniform Resource Locator

a URL specifies the location of a resource on the internet  
It's widely used in HTTP Protocol

## Example

```url
protocol://username:password@host:port/path?query#fragment
```

### username and password

Authentication params  
Nowadays they usually aren't used in HTTP Protocol, but used in others protocols like postgresql

### port

Specifies the port on which the server is listening.  
Default ports: 80 for HTTP, 443 for HTTPS

### host

Refers to the domain name or IP address of the server hosting the resource.

`subdomain.domain.tld`

#### subdomain

Any subdomains in the same domain  
Each subdomain can point to a completely different server

##### example

`docs.google.com`  
`mail.google.com`

#### domain

Main domain

#### tld

Stands for Top-level domain  
used by DNS Root level Servers to locate the IP address of the server

## HTTP Sessions

-   Authentication
-   Authorization

Analogy




