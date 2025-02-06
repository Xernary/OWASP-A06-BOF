# OWASP-A06-BOF

Showcase of an example of OWASP A06 "Vulnerable and Outdated Components" via a web service using a C library vulnerable to Buffer Overflow

<br />

## Server

The vulnerable server runs in a docker container, the image can be created using the Dockerfile, running this in the same folder of it:
```
docker build --tag 'rop-server' . 
```

<br />


The container can then be created and ran using:
```
docker run --network=host -it rop-server
```
<br />


PHP server setup:
```
apt install php
php -S <server-ip>:8080 &
```
<br />

## Exploit

To run the script that spawns a shell locally:
```
python3 exploit.py LOCAL
```
or 
```
python3 exploit.py
```
to run it on a remote server.



