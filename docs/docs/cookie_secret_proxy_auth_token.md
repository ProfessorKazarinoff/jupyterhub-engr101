# Create a Cookie Secret and Proxy Auth Token

In addition to an SSL certificate, the [Jupyter Hub docs on security basics](http://jupyterhub.readthedocs.io/en/latest/getting-started/security-basics.html) specify that a cookie secret and poxy auth token be created. 

[TOC]

## Create a Cookie Secret

According to the JupyterHub docs, the cookie secret file should be saved in the ```/srv/jupyterhub``` directory.  ```cd``` into the ```/srv``` directory and ```mkdir``` a new ```jupyterhub``` subdirectory. Note you need to use ```sudo``` to create a subdirectory in ```/srv```.

```text
$ cd /srv
$ sudo mkdir jupyterhub
$ cd jupyterhub
```

Next use touch to create the ```jupyterhub_cookie_secret``` file. Write to the file using ```openssl```. Change the final file permissions to ```600``` as noted in the JupyterHub docs.

```text
$ pwd
/srv/jupyterhub
$ sudo touch jupyterhub_cookie_secret
$ sudo chown :sudo jupyterhub_cookie_secret
$ sudo chmod g+rw jupyterhub_cookie_secret
$ sudo openssl rand -hex 32 > jupyterhub_cookie_secretl
$ sudo chmod 600 jupyterhub_cookie_secret
$ls -la

-rw------- 1 root sudo   65 Feb  6 20:37 jupyterhub_cookie_secret
```

I had trouble with the cookie secret file because I missed where the [jupyterhub docs](http://jupyterhub.readthedocs.io/en/latest/getting-started/security-basics.html#generating-and-storing-as-a-cookie-secret-file) show:

> The file must not be readable by group or other or the server won’t start. The recommended permissions for the cookie secret file are 600 (owner-only rw).

After you create the cookie secret file, note of the file's location. We'll add the ```jupyterhub_cookie_secret``` file location to our JupyterHub configuration.

## Create Proxy Auth Token

To generate the proxy auth token, use the same set of commands used to create the cookie secret, except point to a different file called ```proxy_auth_token```.

```text
$ pwd
/srv/jupyterhub
$ sudo touch proxy_auth_token
$ sudo chown :sudo proxy_auth_token
$ sudo chmod g+rw proxy_auth_token
$ sudo openssl rand -hex 32 > proxy_auth_token
$ sudo chmod 600 proxy_auth_token
$ls -la

-rw------- 1 root sudo   65 Feb  6 20:37 jupyterhub_cookie_secret
-rw------- 1 root sudo   65 Feb  6 20:37 proxy_auth_token
```

Now, when we list the contents of ```~/srv/jupyterhub``` we see:

```
/srv/jupyterhub/
├── jupyterhub_cookie_secret
└── proxy_auth_token
```

## Create dhparam.pem

Let's also generate a ```dhparam.pem``` file. I'm still not exactly sure what the ```dhparam.pem``` file is, it has something to do with security. ```dhparam.pem``` will be incorporated into our Nginx config file later on.

We'll use the same set of commands we used to create the cookie secret and proxy auth token. The part which is different is the ```openssl dhparam``` command generates the ````.pem file```. It takes a minute or two for openssl to do it's work. Finally we modify the permissions again to ```600``` (owner-only rw). Note the location of the ```dhparam.pem``` file as we will add it to the Nginx config file.

```text
$ pwd
/srv/jupyterhub
$ sudo touch dhparam.pem
$ sudo chown :sudo dhparam.pem
$ sudo chmod g+rw dhparam.pem
$ sudo openssl dhparam -out /srv/jupyterhub/dhparam.pem 2048
# wait a minute or two

$ sudo chmod 600 dhparam.pem
$ ls -la

-rw------- 1 root sudo  424 Feb  6 20:37 dhparam.pem
-rw------- 1 root sudo   65 Feb  6 20:37 jupyterhub_cookie_secret
-rw------- 1 root sudo   65 Feb  6 20:37 proxy_auth_token
```

We now have three files in the ```/srv/jupyterhub/``` directory. The ```jupyterhub_cookie_secret``` and ```proxy_auth_token``` will be referenced in the ```jupyterhub_config.py``` file. The ```dhparam.pem``` file will be referenced in the ```nginx.conf``` file.

```text
/srv/jupyterhub/
├── dhparam.pem
├── jupyterhub_cookie_secret
└── proxy_auth_token
```

## Summary

In this section, we created a ```jupyterhub``` directory inside ```/srv```. Inside that directory we created three files using the openssl utility:

 * ```jupyterhub_cookie_secret```
 * ```proxy_auth_token```
 * ```dhparam.pem```

Each of these three files have their permissions set to ```600```.

## Next Steps

The next step is to install Nginx on the server.

<br>