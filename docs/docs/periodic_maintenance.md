# Periodic Maintenance

After running JupyterHub for two quarters there are a couple lessons I've learned about maintenance.

## Increase server size before class starts

Right at the start of class, when everyone logs in, the server can get overloaded. So during only those class times when 24 students plus 1 instructor will all be on the JupyterHub server at the same time, boost the server size to a $40/month or maybe even up to an $80/month server. You can update the server size at the Digital Ocean Dashboard, but the server has to be shut down first at the command line.

```text
$ sudo systemctl stop jupyterhub
$ sudo systemctl status jupyterhub
# [Ctrl]+[c] to exit
$ sudo systemctl stop nginx
$ sudo systemctl status nginx
# [Ctrl]+[c] to exit

$ sudo shutdown -h now
```

Log onto Digital Ocean and select the project and server running JupyterHub. Make sure the "power slider" is set to [off]. Then select the $80/month server and click [Upgrade Server]. Now many students should be able to log in and run JupyterHub at the same time. 

**Then remeber to drop the server size back down after class ends.**

You don't want to rack up a huge bill with Digital Ocean. During the rest of the regular week (not during class time), the server can be smaller and cheaper becuase only a few users at a time will be logged in at the same time. 

## Restart server once a week

The Hub has seemed to get sluggish when it has been running for a long time continously. Shutting the down JupyterHub, Nginx, then restarting the server once each week is a good idea. To restart the server, first log into JupyterHub and shut down all the servers. The from the command line, run :

```text
$ sudo systemctl stop jupyterhub
$ sudo systemctl status jupyterhub
# [Ctrl]+[c] to exit
$ sudo systemctl stop nginx
$ sudo systemctl status nginx
# [Ctrl]+[c] to exit

$ sudo shutdown -h now
```

Then go to the Digital Ocean dashboard and restart the server. After the server restarts, restart nginx then JupyterHub.

```text
$ sudo systemctl start nginx
$ sudo systemctl status nginx
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
```

## Extras

There are a couple extra docs pages. Browse through these if you want to use the JupyterLab interface, include a GitHub in the JupyterLab interface or try and make the regular domain name go to the nbgitpuller domain name.

<br>
 