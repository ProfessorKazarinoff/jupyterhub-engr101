# Run JupyterHub as a system service

Running JupyerHub as a system service allows JupyterHub to run continuously even if we are not logged into the server. It also keeps JupyterHub running while when we log into the server and make any changes.

[TOC]

To run JupyterHub as a system service (according to [this wiki](https://github.com/jupyterhub/jupyterhub/wiki/Run-jupyterhub-as-a-system-service)
), we need to create a service file in the ```/etc/systemd/system``` directory. ```cd``` into the directory and have a look around. We see a couple files that end in ```.service```.

```text
$ cd /etc/systemd/system
$ ls
cloud-init.target.wants                network-online.target.wants
dbus-org.freedesktop.thermald.service  paths.target.wants
default.target.wants                   sockets.target.wants
final.target.wants                     sshd.service
getty.target.wants                     sysinit.target.wants
graphical.target.wants                 syslog.service
iscsi.service                          timers.target.wants
multi-user.target.wants
```

Create a new ```.service``` file called ```jupyterhub.service```

```text
pwd
/etc.systemd/system
$ sudo nano jupyterhub.service
```

In the ```jupyterhub.service``` file, add the following. Note that as part of the ```PATH``` environment variable ```/opt/miniconda3/envs/jupyterhub/bin/``` is included. This is the path to our virtual environment. As part of the ```ExecStart= ``` section, we include a flag for our JupyterHub config file located at  ```/etc/jupyterhub/jupyterhub_config.py```. 

```text
[Unit]
Description=JupyterHub
After=syslog.target network.target

[Service]
User=root
Environment="PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/miniconda3/envs/jupyterhub/bin/"
ExecStart=/opt/miniconda3/envs/jupyterhub/bin/jupyterhub -f /etc/jupyterhub/jupyterhub_config.py

[Install]
WantedBy=multi-user.target
```

Save and exit the nano text editor with [Ctrl]+[x] and [y] then [Enter]. 

Now we need to reload the system daemon. After the system daemon is reloaded, we can run JupyterHub as a system service using the command: ```sudo systemctl <start|stop|status> jupyterhub```

```text
$ sudo systemctl daemon-reload
$ sudo systemctl start jupyterhub
```

We can see if JupyterHub is running with:

```text
$ sudo systemctl status jupyterhub

 Loaded: loaded (/etc/systemd/system/jupyterhub.service; 
 Active: active (running)
```

<br>

## Test local OAuth

Now we can point a web browser at our domain name and log into JupyterHub as our non-root user ```peter``` and the password we set for ```peter``` on the server. This time we are running with SSL security in place and even if we browse to ```http://mydomain.com```, Nginx will forward us to ```https://mydomain.com```.

The JupyterHub login screen looks something like the screen capture below:

![JupyterHub PAM Login](images/jupyterhub_pam_spawner_login.png)

A couple times I thought that JupyterHub was running after using ```systemctl start jupyterhub```, but the JupyterHub wasn't working when I went to the server's web address. It turned out that JupyterHub wasn't running when I keyed in ```systemctl status jupyterhub```. Most times looking for an error and tracking down the the error worked, but one time it seemed to be a problem with the http-configurable-proxy. 

The following command will shut down the proxy if you get stuck like I did (insert the number corresponding to the configurable-http-proxy process after the ```kill``` command):

```text
$ ps aux | grep configurable-http-proxy
$ kill #### 
```

## Summary

In this section, we got JupyterHub running as a system service. We created a ```jupyterhub.service``` file in the ```/etc/systemd/system/``` directory and made sure to include the PATH to our ```(jupyterhub)``` virtual environment and the path to our ```jupyterhub_config.py``` file. Finally, we reloaded the system service daemon and started the JupyterHub service. Then be opened a web browser and keyed in our domain name and logged into JupyterHub. 

## Next Steps

The next step is to have JupyterHub accept GitHub usernames and passwords. This will allow students with Github accounts to log into JupyterHub and means we don't have to deal with creating new users and sending students usernames and passwords.

<br>
