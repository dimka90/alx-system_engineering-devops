ou have been provided with two additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
The goal is to improve the web stack by introducing redundancy for the web servers. This will enhance the system's capacity to handle more traffic and increase overall reliability. The redundancy ensures that if one web server fails, the other can continue to handle incoming requests.

For this project, you are required to write Bash scripts that automate the configuration of a brand new Ubuntu server to meet the specified task requirements. The tasks involve setting up Nginx with a custom response header, doubling the number of web servers, and installing and configuring HAProxy as a load balancer.

Resources
Introduction to load-balancing and HAproxy
HTTP header
Debian/Ubuntu HAProxy packages
Requirements
General
Allowed Editors: vi, vim, emacs
Operating System: Ubuntu 16.04 LTS
File Endings: All files should end with a new line
README.md: A README.md file, at the root of the project folder, is mandatory
Bash Scripts: All Bash script files must be executable
Shellcheck: Your Bash script must pass Shellcheck (version 0.3.7) without any error
Shebang: The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
Comments: The second line of all your Bash scripts should be a comment explaining what the script is doing
Servers
Name	Username	IP	State
359081-web-01	ubuntu	34.207.253.36	running
359081-web-02	ubuntu	100.25.166.148	running
359081-lb-01			
Tasks
Task 0: Double the number of webservers
Requirements:

Configure Nginx on web-02 to be identical to web-01.
Add a custom Nginx response header:
Name: X-Served-By
Value: The hostname of the server Nginx is running on
Write a Bash script 0-custom_http_response_header to configure a new Ubuntu machine to meet the requirements of this task.
Ignore Shellcheck rule SC2154.
Example:

bash
Copy code
$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
Task 1: Install your load balancer
Requirements:

Install and configure HAProxy on lb-01.
Configure HAProxy to send traffic to web-01 and web-02.
Distribute requests using a round-robin algorithm.
Ensure that HAProxy can be managed via an init script.
Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.
Example:

bash
Copy code
$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes
Repository:

GitHub Repository
Directory: 0x0F-load_balancer
Files: 1-install_load_balancer
