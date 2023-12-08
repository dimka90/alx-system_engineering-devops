0-world_wide_web
Description
This Bash script is designed to configure your domain zone, adding specific subdomains and pointing them to corresponding IP addresses. Additionally, the script can display information about the subdomains using dig, awk, and other command-line utilities.

Requirements
Add the subdomain www to your domain and point it to your load-balancer IP (lb-01).
Add the subdomains lb-01, web-01, and web-02 to your domain, pointing them to the respective IPs.
The Bash script must accept two arguments:
domain: Domain name to audit (mandatory).
subdomain: Specific subdomain to audit (optional).
Output format: "The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]."
When only the domain parameter is provided, display information for its subdomains in the order www, lb-01, web-01, and web-02.
When passing both domain and subdomain parameters, display information for the specified subdomain.
Ignore ShellCheck case SC2086.
Must use awk and include at least one Bash function.
Examples
bash
Copy code
$ ./0-world_wide_web holberton.online
The subdomain www is an A record and points to 54.210.47.110
The subdomain lb-01 is an A record and points to 54.210.47.110
The subdomain web-01 is an A record and points to 34.198.248.145
The subdomain web-02 is an A record and points to 54.89.38.100
bash
Copy code
$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is an A record and points to 54.89.38.100
Repository Information
GitHub Repository: alx-system_engineering-devops
Directory: 0x10-https_ssl
File: 0-world_wide_web
1-haproxy_ssl_termination
Description
This configuration file (haproxy.cfg) is designed for HAproxy SSL termination. It means that HAproxy is configured to handle encrypted traffic, decrypt it, and pass it on to its destination. The configuration includes settings to:

Listen on port TCP 443
Accept SSL traffic
Serve encrypted traffic that returns the root page of your web server, containing "Holberton School."
Requirements
HAproxy must be installed with version 1.5 or higher (SSL termination is not available before v1.5).
HAproxy must be configured to listen on port TCP 443.
HAproxy must accept SSL traffic.
The root page of your domain must contain "Holberton School."
Example
bash
Copy code
$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
bash
Copy code
$ curl https://www.holberton.online
Holberton School for the win!
Repository Information
GitHub Repository: alx-system_engineering-devops
Directory: 0x10-https_ssl
File: 1-haproxy_ssl_termination
