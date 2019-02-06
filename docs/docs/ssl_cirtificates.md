# Obtain SSL Certificates

Now that a domain name is hooked up to our JupyterHub server, we'll be able to obtain an SSL certificate and run JupyterHub over https. I followed [this presentation](https://www.slideshare.net/willingc/jupyterhub-tutorial-at-jupytercon) to install **certbot**, a program used to generate SSL certificates.

[TOC]

## Install and run certbot

We'll use **certbot** to obtain a standalone SSL certificate. Log onto the server with PuTTY.

Certbot will need to communicate over the network, so before we run certbot, we need to open up Port 80 using the ufw firewall utility.

```text
$ sudo ufw allow 80
```

The commands below installs certbot, modifies permissions, and runs certbot to obtain the SSL certificate. Make sure to change ```mydomain.org``` to the correct domain name.

```text
$ cd ~
$ mkdir certbot
$ cd certbot
$ wget https://dl.eff.org/certbot-auto
$ chmod a+x certbot-auto
$ ./certbot-auto certonly --standalone -d mydomain.com
```

Certbot will ask you for an email address where it will send certificate renewal notices.

```text
Enter email address (used for urgent renewal and security notices) (Enter 'c' to cancel):
```

Agree to the licencing terms by typing ```A```. You not need to share an email address with the ```Electronic Frontier Foundation```. Getting an email that it is time to renew the SSL certificate like we did above is a good idea though.

If Certbot worked, and we get our SSL certificates- the output looks something like below:

```text
IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/engr101lab.org/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/engr101lab.org/privkey.pem
   Your cert will expire on 2019-05-07. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot-auto
   again. To non-interactively renew *all* of your certificates, run
   "certbot-auto renew"
```

Note the date when the certificate expires. You will need to log back onto the server before this date and run ```certbot-auto renew``` to update the SSL cirt in a few months time.

Now that Certbot created our SSL certs, we can close Port 80 using the ufw utility.

```text
$ sudo ufw deny 80
```

## File Locations and Permissions

Note the location of the ```fullchain.pem``` and ```privkey.pem``` files. We'll need to put these file paths into our Nginx configuration.

We also need to allow Nginx access these ```.pem``` files. I had trouble getting Nginx to run and [this presentation](https://www.youtube.com/watch?v=alaGteCPZU8&t=1721s) showed a way to give Nginx access to the SSL key files. There is probably a more "Linuxy" way of giving Nginx access to the cert files, but I messed around with the permission settings for a while, and using the commands below worked.

```text
$ cd /etc
$ cd letsencrypt
$ ls -la

$ sudo chown :sudo -R archive/
$ sudo chown :sudo -R live/
$ sudo chmod 600 -R archive/
$ sudo chmod 600 -R live/
$ ls -la

drwxr-xr-x  9 root root 4096 Feb  6 17:41 .
drwxr-xr-x 92 root root 4096 Feb  6 17:36 ..
drwx------  3 root root 4096 Feb  6 17:36 accounts
drw-------  3 root sudo 4096 Feb  6 17:41 archive
drwxr-xr-x  2 root root 4096 Feb  6 17:41 csr
drwx------  2 root root 4096 Feb  6 17:41 keys
drw-------  3 root sudo 4096 Feb  6 17:41 live
drwxr-xr-x  2 root root 4096 Feb  6 17:41 renewal
drwxr-xr-x  5 root root 4096 Feb  6 17:36 renewal-hooks

```

## Summary

In this section, we installed Certbot on the server and ran Cerbot to obtain an SSL certificate. One gotcha to remember is that Port 80 must be open to download Certbot. Port 80 also has to be open when Certbot runs. After we obtained our SSL certificate, we noted the location of the the ```fullchain.pem``` and ```privkey.pem``` files Certbot created. Finally, we changed the permissions of the directories that house the ```.pem``` files: ```/etc/letsencrypt/archive/``` and ```/etc/letsencrypt/archive/```.

## Next Steps

The next step is to create a cookie secret, proxy auth token, and dhparem.pem file.

<br>